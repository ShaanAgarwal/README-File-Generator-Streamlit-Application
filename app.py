import streamlit as st
import readme_generator as rg

st.title = "README Generator With The Help Of ChatGPT"

uploaded_file = st.file_uploader("Upload Code File")

if uploaded_file is not None:
    content = uploaded_file.read().decode()
    response = rg.ask(f"{content}\n\nRead the code and generate a README.md in markdown format.")
    st.markdown(response)