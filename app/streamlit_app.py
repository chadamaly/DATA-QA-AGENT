import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from main import answer

st.set_page_config(page_title="Data Q&A Agent")

st.title("Superstore.csv Data Q&A Agent")
st.write("Ask a question in plain English about sales, customers, or products.")

question = st.text_input("Your question:", placeholder="E.g. Which customer spent the most?")

if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        sql, response = answer(question)
    st.success(sql)
    st.success(response)

st.markdown("---")
st.caption("Example questions: 'How many sales in total?', "
           "'Which product sells best?', 'What's the total profit by category?'")