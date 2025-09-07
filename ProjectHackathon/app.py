import streamlit as st
from search import search_web
from extract import extract_content



st.title("Mr. Researcher")
st.markdown("#### Ask me anything, and I’ll dig up the best insights from across the web.")

query = st.text_input("What topic are you researching today?")
time_filter = st.selectbox("Time range", ["Any", "Past week", "Past month", "Past year"])
tone = st.selectbox("Tone of summary", ["Neutral", "Technical", "Simplified", "Conversational"])

if st.button("Start Research", key="start_button"):
    if not query:
        st.warning("Please enter a topic to research.")
    else:
        st.info(f"Searching for {query} with tone {tone} and time filter {time_filter}...")
        urls = search_web(query)

        if not urls:
            st.error("No results found. Try a different topic or time range.")
        else:
            st.markdown("Top Articles Found:")
            for i, url in enumerate(urls):
                content = extract_content(url)
                st.markdown(f"{i+1}. {content['title']}")
                st.write(content['text'][:500] + "...")
                if content['publish_date']:
                    st.write(f"Published on: {content['publish_date']}")
                st.write(f"[Read Full Article]({url})")
                st.markdown("---")   