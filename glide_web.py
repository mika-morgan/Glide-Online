import streamlit as st
import time

st.set_page_config(page_title="Glide IDE", page_icon="🧩", layout="wide")
st.set_page_config(page_title="Glide Web IDE", layout="wide")
st.title("🧩 GLIDE")

# Initialize session state for inserting code
if "code_to_insert" not in st.session_state:
    st.session_state.code_to_insert = ""

# Sidebar Toolbox – Always Visible
st.sidebar.title("Toolbox")

# --- Category: Basics ---
with st.sidebar.expander("Basics", expanded=True):
    if st.button("Print Hello"):
        st.session_state.code_to_insert = "print('Hello, world!')"
    if st.button("Set Variable"):
        st.session_state.code_to_insert = "x = 5"

# --- Category: Conditionals ---
with st.sidebar.expander("Conditionals", expanded=False):
    if st.button("If Statement"):
        st.session_state.code_to_insert = "x = 10\nif x > 5:\n    print('x is greater than 5')"
    if st.button("If/Else Statement"):
        st.session_state.code_to_insert = "x = 10\nif x > 5:\n    print('Big')\nelse:\n    print('Small')"

# --- Category: Loops ---
with st.sidebar.expander("Loops", expanded=False):
    if st.button("For Loop"):
        st.session_state.code_to_insert = "for i in range(5):\n    print(i)"
    if st.button("While Loop"):
        st.session_state.code_to_insert = "x = 0\nwhile x < 5:\n    print(x)\n    x += 1"

# --- Category: Functions ---
with st.sidebar.expander("Functions", expanded=False):
    if st.button("Define Function"):
        st.session_state.code_to_insert = "def greet():\n    print('Hello')"
    if st.button("Function with Args"):
        st.session_state.code_to_insert = "def greet(name):\n    print(f'Hello, {name}')"

# --- Code Editor (Main Panel) ---
st.title("Glide Code Editor")
code_input = st.text_area("Your Code:", height=300, value=st.session_state.code_to_insert)

# Update session state with latest code
st.session_state.code_to_insert = code_input

# Run the code
if st.button("Run Code"):
    try:
        exec(code_input, {})
    except Exception as e:
        st.error(f"Error: {e}")


# --- Code Editor ---
st.subheader("Code Editor")
if "editor" not in st.session_state:
    st.session_state.editor = ""


code_input = st.text_area("Write your code here:", height=300, value=st.session_state.editor, key="code_area")


# --- Run Code ---
col1, col2 = st.columns([1, 6])
with col1:
    run_button = st.button("▶️ Run Code")


# --- Output Panel ---
st.subheader("Output")
output_area = st.empty()


if run_button:
    try:
        # Capture output
        import io
        import contextlib


        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exec(code_input, {})
        output = buffer.getvalue()
        output_area.code(output, language="text")
    except Exception as e:
        output_area.code(f"Error:\n{e}", language="text")
