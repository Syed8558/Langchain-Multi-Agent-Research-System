from src.agents.agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain
)


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # ==========================================
    # Step 1: Search Agent
    # ==========================================

    print("\n" + "=" * 20)
    print("Step 1 - Search agent is working...")
    print("=" * 20)

    search_agent = build_search_agent()

    search_results = search_agent.invoke(
        {
            "messages": [
                (
                    "user",
                    f"Find recent, reliable and detailed information on the topic: {topic}"
                )
            ]
        }
    )

    state["search_results"] = search_results["messages"][-1].content

    print("\nSearch Results:\n")
    print(state["search_results"])

    # ==========================================
    # Step 2: Reader Agent
    # ==========================================

    print("\n" + "=" * 20)
    print("Step 2 - Reader agent is scraping...")
    print("=" * 20)

    reader = build_reader_agent()

    reader_result = reader.invoke(
        {
            "messages": [
                (
                    "user",
                    f"""
Based on the search results about {topic},
pick the most relevant URLs and scrape information.

Search Results:
{state["search_results"][:800]}
"""
                )
            ]
        }
    )

    state["scraped_info"] = reader_result["messages"][-1].content

    print("\nScraped Info:\n")
    print(state["scraped_info"])

    # ==========================================
    # Step 3: Writer Chain
    # ==========================================

    print("\n" + "=" * 20)
    print("Step 3 - Writer agent is drafting report...")
    print("=" * 20)

    research_combined = f"""
Search Results:
{state["search_results"]}

Scraped Info:
{state["scraped_info"]}
"""

    state["report"] = writer_chain.invoke(
        {
            "topic": topic,
            "research": research_combined
        }
    )

    print("\nFinal Report:\n")
    print(state["report"])

    # ==========================================
    # Step 4: Critic Chain
    # ==========================================

    print("\n" + "=" * 20)
    print("Step 4 - Critic agent evaluating report...")
    print("=" * 20)

    state["feedback"] = critic_chain.invoke(
        {
            "report": state["report"]
        }
    )

    print("\nFeedback:\n")
    print(state["feedback"])

    return state



