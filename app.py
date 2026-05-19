import streamlit as st

from rag_pipeline import ask_question

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Upwork API Technical Support Bot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------
# Custom CSS
# -----------------------------------
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0.3rem;
}

.sub-title {
    text-align: center;
    color: #A0A0A0;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.stTextInput > div > div > input {
    font-size: 16px;
}

.source-box {
    background-color: #111827;
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #2A2A2A;
    margin-bottom: 1rem;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Header
# -----------------------------------
st.markdown(
    '<div class="main-title">🤖 Upwork API Technical Support Bot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Grounded RAG-based assistant for answering Upwork API technical queries.</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# Input Section
# -----------------------------------
query = st.text_input(
    "Enter your technical question:",
    placeholder="Example: How long is an OAuth access token valid for?"
)

# -----------------------------------
# Submit Button
# -----------------------------------
if st.button("Submit Query"):

    if not query.strip():

        st.warning("Please enter a valid question.")

    else:

        with st.spinner("Retrieving documentation and generating response..."):

            answer, sources, latency = ask_question(query)

        st.divider()

        # -----------------------------------
        # Answer Section
        # -----------------------------------
        st.subheader("Answer")

        st.write(answer)

        st.divider()

        # -----------------------------------
        # Sources Section
        # -----------------------------------

        if len(sources) > 0:
            st.subheader("Retrieved Sources")

            
            for source in sources:

                with st.expander(
                    f"Source {source['source_number']}",
                    expanded=False
                ):

                    st.code(
                        source["content"],
                        language="text"
                    )

        st.divider()

        # -----------------------------------
        # Latency Section
        # -----------------------------------
        st.subheader("API Latency")

        st.metric(
            label="Response Time",
            value=f"{latency} sec"
        )

# -----------------------------------
# Footer
# -----------------------------------
st.divider()

st.caption(
    "Built using LangChain, ChromaDB, Streamlit, and DeepInfra Llama 3.1"
)