import streamlit as st
import io
import contextlib

st.set_page_config(layout="wide")
st.title("Glide IDE")

# Remove blank space at top of page
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem !important;
        }
    <style>
        h3 {
            margin-bottom: 0.25rem;
        }
        .stCodeBlock {
            margin-top: 0.25rem;
        }
    </style>
    </style>
    """,
    unsafe_allow_html=True
)

# --- Session state ---
if "code_editor_text" not in st.session_state:
    st.session_state.code_editor_text = ""

# --- Toolbox Commands ---
toolbox = {
    "Basics": {
        "Comment": "# This is a comment\n\n",
        "Print": "print('Hello, world!')\n\n",
        "Make Variable": "name = 'Mika'\n\n",
        "Make multiple Variables": "x, y, z = 1, 2, 3\n\n",
        "Input": "name = input('What is your name? ')\n\n",
    },
    "Math Operations": {
        "Addition": "x = 5 + 3\nprint('Result:', x)\n\n",
        "Subtraction": "x = 10 - 4\nprint('Result:', x)\n\n",
        "Multiplication": "x = 6 * 7\nprint('Result:', x)\n\n",
        "Division": "x = 20 / 4\nprint('Result:', x)\n\n",
        "Integer Division": "x = 20 // 3\nprint('Result:', x)\n\n",
        "Remainder": "x = 10 % 3\nprint('Result:', x)\n\n",
        "Exponentiation": "x = 2 ** 3\nprint('Power:', x)\n\n",
        "Increment by value": "x = 1\nx += 1\nprint(x)\n\n",
        "Decrement by value": "x = 2\nx -= 1\nprint(x)\n\n"
    },
    "Conditionals": {
        "if Statement": "if x > 5:\n    print('x is greater than 5')\n\n",
        "if-else Statement": "if x > 5:\n    print('x is big')\nelse:\n    print('x is small')\n\n",
        "if-elif-else Statement": (
            "if x > 5:\n    print('x > 5')\n"
            "elif x == 5:\n    print('x = 5')\n"
            "else:\n    print('x < 5')\n\n"
        )
    },
    "Loops": {
        "For loop": "for item in [1, 2, 3]:\n    print(item)\n\n",
        "Range with stop": "for i in range(5):\n    print(i)\n\n",
        "Range with start & stop": "for i in range(1, 5):\n    print(i)\n\n",
        "Range with start, stop, step": "for i in range(1, 10, 2):\n    print(i)\n\n",
        "While loop": "x = 0\nwhile x < 5:\n    print(x)\n    x += 1\n\n",
        "Nested loop": (
            "for i in range(2):\n"
            "    for j in range(3):\n"
            "        print(i, j)\n\n"
        ),
        "Do-While loop": (
            "while True:\n"
            "    x = input('Enter q to quit: ')\n"
            "    if x == 'q':\n"
            "        break\n\n"
        )
    },
    "Functions": {
        "Define Fruitless Function": (
            "def greet(name):\n"
            "    print('Hello', name)\n\n"
        ),
        "Define Fruitful Function": (
            "def add(x, y):\n"
            "    return x + y\n\n"
        ),
        "Function Call": "greet('Mika')\n\n"
    }
}

# --- Toolbox Sidebar ---
st.sidebar.title("Toolbox")
for category, commands in toolbox.items():
    with st.sidebar.expander(category, expanded=(category == "Basics")):
        for label, code in commands.items():
            if st.button(label, key=label):
                st.session_state.code_editor_text += code

# --- Main Editor ---
st.subheader("Code Editor")

# --- Run Code ---
if st.button("Run Code"):
    output_buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code_input, {})
    except Exception as e:
        output_buffer.write(str(e))
    st.subheader("Output")
    st.code(output_buffer.getvalue())
