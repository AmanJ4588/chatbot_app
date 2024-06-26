import streamlit as st

st.set_page_config(layout="wide") 
st.write("### 🤖 Client Retention Model")


with st.sidebar:
    if st.button("New Chat"):
        st.session_state["messages"] = {}  

# Initialize messages in session state if not already set
if ("messages" not in st.session_state) or (st.session_state["messages"] == {}):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]


# Display existing chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
# Get user input and handle empty input
if prompt := st.chat_input("Enter your query"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    #response coming from the backend 
    msg = "I'm still under development and can't generate responses yet"
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)