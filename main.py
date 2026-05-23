from src.tools.tools import web_search ,scrape_url

# web_search_result=web_search.invoke(
#     {"query":"Latest news on AI research in 2026?"})

# print(web_search_result)

scrape_result=scrape_url.invoke({"url":"https://www.infotech.com/research/ss/ai-trends-2026"})
print(scrape_result)