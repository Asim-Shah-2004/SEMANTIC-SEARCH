import streamlit as st

st.title("Echo Bot")

# Function to clear the chat display
def clear_chat_display():
    for _ in range(len(st.session_state.messages)):
        st.empty()

# Check if "messages" exists in the session state, if not initialize it as an empty list
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages from the session state
for message in st.session_state.messages:
    with st.empty():
        st.write(f"{message['role']}: {message['content']}")

# Get input from the user
prompt = st.text_input("Type a message...")

# If user inputs a message, add it to the session state and echo back the message
if prompt:
    st.session_state.messages.append({"role": "User", "content": prompt})

    # Clear the chat display before appending new messages
    clear_chat_display()

    # Echo back the user input
    st.session_state.messages.append({"role": "Echo Bot", "content": prompt})
