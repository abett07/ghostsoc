import streamlit as st
import requests

st.set_page_config(page_title="GhostSOC Deception Engine", layout="wide")
st.title("👻 GhostSOC – AI-Powered Fake SSH Terminal")

# Input box
user_input = st.text_input("Attacker Command", placeholder="e.g., ls -la")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a command.")
    else:
        # Send to FastAPI backend
        try:
            response = requests.post("http://127.0.0.1:8000/simulate", json={"input": user_input})
            result = response.json().get("response", "[No response]")
            st.code(result, language="bash")
        except Exception as e:
            st.error(f"Error: {e}")
