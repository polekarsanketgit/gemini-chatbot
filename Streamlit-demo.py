#===============================================
#   To run this code run below line in terminal 
#   python -m streamlit run demo.py 
#===============================================

import streamlit as st
import pandas as pd


st.text("st.text(): Shows plain, fixed-width text (good for simple messages).")

st.write("st.write(): More flexible—displays text, numbers, data, even charts.")

prompt = st.text_input("Enter your prompt:")
if prompt:
    st.write(f"Hello, {prompt}!")

llm = st.selectbox(
    "Pick an LLM you've used or want to explore:",
    ["GPT-3.5", "GPT-4", "Claude 3", "Mistral 7B"]
)
st.write(f"You selected: {llm}")

if st.button("Send"):
    st.write("Button clicked!")

message = st.text_area("Type your message here:", height=120)
if message:
    st.write(f"You wrote: {message}")

enable_agent_mode = st.checkbox("Enable Autonomous Agent Mode")
if enable_agent_mode:
    st.write("✅ Agent Mode is now active.")

temperature_mode = st.radio(
    "Select Temperature Setting:",
    ["Stable (0.2)", "Balanced (0.7)", "Creative (1.0)"]
)
st.write(f"Model set to: {temperature_mode}")

token_limit = st.slider("Max token limit:", 100, 4000, 512)
st.write(f"LLM will respond with up to {token_limit} tokens.")

num_agents = st.number_input(
    "How many parallel agents to run?", min_value=1, max_value=10, step=1
)
st.write(f"Running {num_agents} agent(s)...")

launch_date = st.date_input("Launch your agent on:")
st.write(f"Scheduled for: {launch_date}")

agent_name = st.sidebar.text_input("Enter Agent Name")
selected_llm = st.sidebar.selectbox("Choose LLM:", ["GPT-4", "Claude 3", "Gemini"])

st.write(f"🤖 Agent {agent_name} using {selected_llm}")

with st.expander("📌 Prompt Engineering Tips"):
    st.write("""
    - Use clear instructions
    - Define model behavior
    - Chain multi-step tasks
    """)

st.markdown('# 🧠 Welcome to AgentForge')
st.markdown('> Your lab to create, configure, and deploy AI agents.')

upload = st.file_uploader("Upload your student data", type=["csv"])

if upload:
    data = pd.read_csv(upload)
    st.subheader("📄 Uploaded student data")
    st.dataframe(data)

if upload:
    st.subheader("📊 Model Call Statistics")
    st.write(data.describe())

