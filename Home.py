__import__("pysqlite3")
import sys
import sqlite3
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import streamlit as st
from utilities.ai_embedding import text_small_embedding
from utilities.ai_inference import gpt4o_mini_inference, gpt4o_mini_inference_yes_no
from utilities.chroma_db import get_or_create_persistent_chromadb_client_and_collection, add_document_chunk_to_chroma_collection, query_chromadb_collection, delete_chromadb_collection
from utilities.documents import read_document
from utilities.layout import page_config

page_config()
#collection, client = get_or_create_persistent_chromadb_client_and_collection("legal docs collection")

st.title("📜 Preliminary Review of Intellectual Property License Agreement")

if "scenario" not in st.session_state:
    st.session_state.scenario = None

# Initialize response for each clause
if "sub_response_scope" not in st.session_state:
    st.session_state.sub_response_scope = None

if "sub_response_duration" not in st.session_state:
    st.session_state.sub_response_duration = None

if "sub_response_restrictions" not in st.session_state:
    st.session_state.sub_response_restrictions = None

if "sub_response_payment" not in st.session_state:
    st.session_state.sub_response_payment = None

if "sub_response_ownership" not in st.session_state:
    st.session_state.sub_response_ownership = None

if "sub_response_termination" not in st.session_state:
    st.session_state.sub_response_termination = None

# Input agreement content
st.session_state.scenario = st.text_area("📝 **Please enter/upload the content of the license agreement or relevant description:**")
# File uploader
uploaded_file = st.file_uploader("📂 **Upload your document (PDF or DOCX):**")
document_content = ''
if uploaded_file is not None:
    # Read the content of the uploaded document
    document_content = read_document(uploaded_file)

# Scope of Authorization check

st.markdown("<h2>1.  Scope of Authorization</h2>", unsafe_allow_html=True)

if st.button("🔍 Check Scope of Authorization"):
    st.session_state.sub_response_scope = gpt4o_mini_inference(
        "You are an expert in intellectual property law.",
        f"""
        Your task is to determine whether the following agreement specifies a clear Scope of Authorization:
        {st.session_state.scenario}+{document_content}
        Provide a clear 'yes' or 'no' on whether the scope of authorization is sufficiently defined, along with an explanation.
        """
    )
if st.session_state.sub_response_scope:
    st.write(f"AI's assessment of the Scope of Authorization: {st.session_state.sub_response_scope}")

# Authorization Duration check

st.markdown("<h2>2. Authorization Duration</h2>", unsafe_allow_html=True)

if st.button("⏳ Check Authorization Duration"):
    st.session_state.sub_response_duration = gpt4o_mini_inference(
        "You are an expert in intellectual property law.",
        f"""
        Your task is to determine whether a clear Authorization Duration is specified in the following agreement:
        {st.session_state.scenario}+{document_content}
        Provide a clear 'yes' or 'no' on whether the duration is adequately defined, along with an explanation.
        """
    )
if st.session_state.sub_response_duration:
    st.write(f"AI's assessment of the Authorization Duration: {st.session_state.sub_response_duration}")

# Usage Restrictions check

st.markdown("<h2>3. Usage Restrictions</h2>", unsafe_allow_html=True)

if st.button("🚫 Check Usage Restrictions"):
    st.session_state.sub_response_restrictions = gpt4o_mini_inference(
        "You are an expert in intellectual property law.",
        f"""
        Your task is to evaluate whether the following agreement includes specific Usage Restrictions:
        {st.session_state.scenario}+{document_content}
        Provide a clear 'yes' or 'no' conclusion on whether there are usage restrictions, with an explanation if applicable.
        """
    )
if st.session_state.sub_response_restrictions:
    st.write(f"AI's assessment of the Usage Restrictions: {st.session_state.sub_response_restrictions}")

# Payment Terms and License Fees check

st.markdown("<h2>4. Payment Terms and License Fees</h2>", unsafe_allow_html=True)

if st.button("💰 Check Payment Terms and License Fees"):
    st.session_state.sub_response_payment = gpt4o_mini_inference(
        "You are an expert in intellectual property law.",
        f"""
        Your task is to determine whether the following agreement specifies Payment Terms and License Fees:
        {st.session_state.scenario}+{document_content}
        Provide a clear 'yes' or 'no' on whether these terms are defined, with an explanation if necessary.
        """
    )
if st.session_state.sub_response_payment:
    st.write(f"AI's assessment of the Payment Terms and License Fees: {st.session_state.sub_response_payment}")

# Intellectual Property Ownership and Usage check

st.markdown("<h2>5. Intellectual Property Ownership and Usage</h2>", unsafe_allow_html=True)

if st.button("📝 Check Intellectual Property Ownership and Usage"):
    st.session_state.sub_response_ownership = gpt4o_mini_inference(
        "You are an expert in intellectual property law.",
        f"""
        Your task is to evaluate whether the agreement specifies Intellectual Property Ownership and Usage Rights:
        {st.session_state.scenario}+{document_content}
        Provide a clear 'yes' or 'no' on whether these terms are defined, along with an explanation.
        """
    )
if st.session_state.sub_response_ownership:
    st.write(f"AI's assessment of the Intellectual Property Ownership and Usage: {st.session_state.sub_response_ownership}")

# Termination Terms check

st.markdown("<h2>6. Termination Terms</h2>", unsafe_allow_html=True)

if st.button("🌼 Check Termination Terms"):
    st.session_state.sub_response_termination = gpt4o_mini_inference(
        "You are an expert in intellectual property law.",
        f"""
        Your task is to evaluate whether the agreement includes Termination Terms:
        {st.session_state.scenario}+{document_content}
        Provide a clear 'yes' or 'no' conclusion on whether termination terms are present, with reasons.
        """
    )
if st.session_state.sub_response_termination:
    st.write(f"AI's assessment of the Termination Terms: {st.session_state.sub_response_termination}")

# Overall conclusion

st.markdown("<h2> Overall Assessment</h2>", unsafe_allow_html=True)

if st.button("🔍 Determine Conclusion"):
    all_responses = [
        st.session_state.get("sub_response_scope"),
        st.session_state.get("sub_response_duration"),
        st.session_state.get("sub_response_restrictions"),
        st.session_state.get("sub_response_payment"),
        st.session_state.get("sub_response_ownership"),
        st.session_state.get("sub_response_termination"),
    ]

    if any(response is None for response in all_responses):
        st.session_state.response = "Please evaluate all clauses before determining the conclusion."
    elif all("yes" in response.lower() for response in all_responses if response):
        st.session_state.response = "The agreement is complete"
    elif any("no" in response.lower() for response in all_responses if response):
        st.session_state.response = "The agreement is incomplete"
    else:
        st.session_state.response = "The status of the agreement is uncertain"

    st.write(f"Overall Assessment: {st.session_state.response}")





