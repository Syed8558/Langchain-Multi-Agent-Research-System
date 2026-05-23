import streamlit as st
from src.pipeline.pipeline import run_research_pipeline

# Page configuration
st.set_page_config(
    page_title=" Intelligent Multi-Agent Research System",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Intelligent Multi-Agent Research System")
st.markdown("Search Agent → Reader Agent → Writer Agent → Critic Agent")

st.divider()

# User Input
topic = st.text_input(
    "Enter a research topic",
    placeholder="Example: Future of Generative AI in Healthcare"
)

# Button
if st.button("Start Research", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a topic.")
    else:

        with st.spinner("Agents are researching..."):

            try:
                result = run_research_pipeline(topic)

                st.success("Research completed!")

                # Search Results
                with st.expander("🔎 Search Results", expanded=True):
                    st.write(result["search_results"])

                # Scraped Information
                with st.expander("📄 Scraped Information", expanded=True):
                    st.write(result["scraped_info"])

                # Final Report
                st.subheader("📝 Final Research Report")
                st.markdown(result["report"])

                # Critic Feedback
                st.subheader("🎯 Critic Feedback")
                st.markdown(result["feedback"])

                # Download report
                st.download_button(
                    label="⬇ Download Report",
                    data=result["report"],
                    file_name="research_report.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")