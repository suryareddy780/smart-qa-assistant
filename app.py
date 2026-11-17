import streamlit as st
from prompt_engine import build_prompt, answer_question

st.set_page_config(page_title="Smart Q&A Assistant", page_icon="💡", layout="wide")
st.title("💡 Smart Q&A Assistant")
st.caption("Explore role prompting, few-shot examples, and different prompt styles.")

with st.sidebar:
    st.header("Configure your assistant")
    role = st.text_input("Assistant role", "You are a helpful tutor")
    style = st.selectbox("Response style", ["Clear and concise", "Step-by-step", "Beginner-friendly", "Detailed", "Socratic"])
    tone = st.selectbox("Tone", ["Friendly", "Professional", "Encouraging", "Neutral"])
    use_examples = st.toggle("Use few-shot examples", value=True)
    st.divider()
    st.subheader("Optional AI connection")
    api_key = st.text_input("OpenAI API key", type="password", help="Optional. Leave blank to use built-in demo mode.")
    model = st.text_input("Model", "gpt-4o-mini")

st.subheader("Ask a question")
question = st.text_area("Your question", placeholder="Example: Explain photosynthesis to a 10-year-old.", height=110)
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("#### Few-shot examples")
    examples = [
        {"question": "What is evaporation?", "answer": "Evaporation is when liquid water changes into water vapor because of heat."},
        {"question": "What is condensation?", "answer": "Condensation is when water vapor cools and changes back into tiny liquid water droplets."},
    ]
    if use_examples:
        for item in examples:
            with st.expander(item["question"], expanded=False):
                st.write(item["answer"])
    else:
        st.info("Few-shot examples are disabled for this question.")
with col2:
    st.markdown("#### Prompt preview")
    if question.strip():
        prompt = build_prompt(role, style, tone, question, examples if use_examples else [])
        st.code(prompt, language="text")
    else:
        st.info("Enter a question to preview the assembled prompt.")

if st.button("Generate answer", type="primary", disabled=not question.strip()):
    with st.spinner("Preparing your answer..."):
        result = answer_question(
            role=role, style=style, tone=tone, question=question,
            examples=examples if use_examples else [],
            api_key=api_key.strip(), model=model.strip()
        )
    st.markdown("### Answer")
    st.write(result["answer"])
    st.caption("Mode: " + result["mode"])
    with st.expander("View complete prompt"):
        st.code(result["prompt"], language="text")

st.divider()
st.caption("Learning project • Role prompting + few-shot prompting + prompt styles")
