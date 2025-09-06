import streamlit as st
import time

st.set_page_config(page_title="Glide IDE", page_icon="🧩", layout="wide")
st.set_page_config(page_title="Glide Web IDE", layout="wide")
st.title("🧩 GLIDE")

# --- Toolbox ---
st.sidebar.header("Toolbox")


code_categories = {
"Basics": {
"Print Hello": "print('Hello, world!')",
"Set Variable": "x = 5"
},
"Conditionals": {
"If Statement": "x = 10\nif x > 5:\n print('x is greater than 5')"
},
"Loops": {
"For Loop": "for i in range(5):\n print(i)"
},
"Functions": {
"Define Function": "def greet(name):\n print(f'Hello, {name}')"
}
}


with st.sidebar.expander("📚 Code Snippets", expanded=True):
    for category, snippets in code_categories.items():
        st.markdown(f"**{category}**")
        cols = st.columns(len(snippets))
        for i, (label, code) in enumerate(snippets.items()):
            if cols[i].button(label, key=f"btn-{category}-{i}"):
                st.session_state.editor += f"\n{code}\n"


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