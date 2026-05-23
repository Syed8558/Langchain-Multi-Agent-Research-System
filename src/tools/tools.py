from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os
from langchain_tavily import TavilySearch

from rich import print
from bs4 import BeautifulSoup
from readability import Document
import trafilatura
import re


load_dotenv()


tavily=TavilySearch(api_key=os.getenv("TAVILY_API_KEY"), max_results=5)


@tool
def web_search(query:str) -> str:
    """ Search the web for the given query and return the results."""

    results= tavily.invoke(query)

    out=[]

    for r in results["results"]:
        out.append(f" Title: {r['title']}\nURL: {r['url']}\ncontent: {r['content'][:300]}\n")
    results="\n".join(out)
    return results





# Convert this function into a LangChain tool
@tool
def scrape_url(url: str) -> str:
    """
    Scrape and extract clean readable content from a URL.
    
    Workflow:
    1. Fetch webpage HTML
    2. Try extracting article content using Trafilatura
    3. If that fails, try Readability
    4. If that fails, use BeautifulSoup as fallback
    5. Return cleaned text
    """

    # Request headers make our script behave like a real browser.
    # Some websites block requests coming from bots.
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        ),

        # Ask website for English content
        "Accept-Language": "en-US,en;q=0.9",

        # Pretend request came from Google
        "Referer": "https://www.google.com/",
    }

    try:

        # =====================================================
        # STEP 1: Fetch webpage
        # =====================================================

        # Send GET request to URL
        response = requests.get(
            url,
            headers=headers,
            timeout=15      # Stop waiting after 15 seconds
        )

        # Raise error if status code is not successful
        # Examples:
        # 404 -> Page not found
        # 500 -> Server error
        response.raise_for_status()

        # Store webpage HTML content
        html = response.text



        # =====================================================
        # STEP 2: Strategy 1 -> Trafilatura extraction
        # Best for articles/blogs/news pages
        # =====================================================

        extracted = trafilatura.extract(
            html,

            # Ignore comment sections
            include_comments=False,

            # Ignore tables
            include_tables=False
        )

        # Verify extraction succeeded
        # and content is meaningful
        if extracted and len(extracted.strip()) > 200:

            # Remove extra spaces/newlines
            cleaned = re.sub(
                r'\s+',
                ' ',
                extracted
            )

            # Return only first 5000 characters
            # Prevent huge text going into LLM
            return cleaned[:5000]



        # =====================================================
        # STEP 3: Strategy 2 -> Readability extraction
        # Used if Trafilatura fails
        # =====================================================

        # Create readability object
        doc = Document(html)

        # Extract main content section
        clean_html = doc.summary()

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(
            clean_html,
            "html.parser"
        )

        # Remove unwanted webpage elements
        # because they usually contain noise
        for tag in soup([
            "script",   # JavaScript
            "style",    # CSS
            "nav",      # Navigation menus
            "footer",   # Footer area
            "header",   # Header area
            "aside",    # Side content
            "form"      # Forms/buttons
        ]):
            tag.decompose()

        # Extract only visible text
        text = soup.get_text(
            separator=" ",
            strip=True
        )

        # Check if useful content exists
        if text and len(text.strip()) > 200:

            # Remove extra whitespace
            cleaned = re.sub(
                r'\s+',
                ' ',
                text
            )

            return cleaned[:5000]



        # =====================================================
        # STEP 4: Strategy 3 -> Full page extraction
        # Last fallback if everything fails
        # =====================================================

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        # Remove unwanted elements
        for tag in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "aside",
            "form"
        ]):
            tag.decompose()

        # Extract all visible text
        text = soup.get_text(
            separator=" ",
            strip=True
        )

        # Remove multiple spaces/newlines
        cleaned = re.sub(
            r'\s+',
            ' ',
            text
        )

        # Return cleaned content if available
        if cleaned:
            return cleaned[:5000]



        # If nothing meaningful found
        return "Could not extract meaningful content from the page."



    # =====================================================
    # Error Handling
    # =====================================================

    # Handle timeout errors
    except requests.exceptions.Timeout:
        return "Request timed out while scraping the URL."


    # Handle HTTP errors
    except requests.exceptions.HTTPError as e:
        return f"HTTP error occurred: {str(e)}"


    # Catch all other unexpected errors
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"



