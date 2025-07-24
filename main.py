import streamlit as st
from streamlit_chat import message
import os
st.set_page_config(page_title="📚 Multi-Doc Chat Assistant", layout="wide")

# ------------------ Sidebar ------------------
with st.sidebar:
    st.title("📂 Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload one or more PDF/DOCX files",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )
    UPLOAD_DIRECTORY = "uploaded_files"
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)
    # Save uploaded files   
    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    if uploaded_files:
        st.success(f"{len(uploaded_files)} document(s) uploaded.")
        for file in uploaded_files:
            st.write(f"📄 {file.name}")
    else:
        st.info("No documents uploaded yet.")
    print(uploaded_files)
    st.markdown("---")
    st.caption("ℹ️ Only layout provided. Logic coming soon, G.")

# ------------------ Main Header ------------------
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color:#4F8BF9;">SmartScraper</h1>
        <p style="color:grey;">Chat with your uploaded PDFs or DOCX files in real-time</p>
    </div>
    <hr style="margin-top: -10px;">
""", unsafe_allow_html=True)

# ------------------ Chat Interface ------------------

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for i, msg in enumerate(st.session_state.messages):
    is_user = msg["role"] == "user"
    message(
        msg["content"],
        is_user=is_user,
        key=str(i),
        avatar_style="big-smile" if is_user else "bottts",
    )

# User input
st.markdown("### 💬 Ask your documents")
user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({
        "role": "assistant",
        "content": "🤖 [AI's response will go here — process the uploaded docs here]"
    })
    st.experimental_rerun()
