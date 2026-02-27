import streamlit as st
import math
from tree import build_balanced_bst
from visualize_streamlit import render_tree_state

st.set_page_config(page_title="BST Guessing Game", layout="wide")

# Custom CSS for a cleaner and more visible look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        font-weight: bold;
        border: 2px solid #ddd;
        transition: all 0.3s ease;
    }
    /* Specific button colors for better visibility */
    div[data-testid="stColumn"]:nth-of-type(1) button {
        background-color: #e8f5e9 !important; /* Light Green */
        color: #2e7d32 !important;
        border-color: #2e7d32 !important;
    }
    div[data-testid="stColumn"]:nth-of-type(2) button {
        background-color: #e3f2fd !important; /* Light Blue */
        color: #1565c0 !important;
        border-color: #1565c0 !important;
    }
    div[data-testid="stColumn"]:nth-of-type(3) button {
        background-color: #fff3e0 !important; /* Light Orange */
        color: #ef6c00 !important;
        border-color: #ef6c00 !important;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar: Config and Logic
with st.sidebar:
    st.title("🛠 Settings")
    min_val = st.number_input("Minimum Value", value=1, step=1)
    max_val = st.number_input("Maximum Value", value=100, step=1)
    
    if st.button("🔄 Reset Game", type="primary"):
        st.session_state.root = build_balanced_bst(min_val, max_val)
        st.session_state.current = st.session_state.root
        st.session_state.path = []
        st.session_state.questions = 0
        st.session_state.game_over = False
        st.session_state.inconsistent = False
        st.session_state.game_started = False
        st.rerun()

    st.divider()
    st.markdown("### 📚 How it works")
    st.info("""
    **BST Construction:**
    The AI builds a balanced Binary Search Tree by picking the median as the root.
    
    **O(log N) Complexity:**
    Each question cuts the search space in HALF. 
    For range 1-100, it takes at most **7 steps**.
    """)
    st.latex(r"\text{Steps} = \lceil \log_2(N) \rceil")

# Initialize session state
if "root" not in st.session_state or st.session_state.get('last_range') != (min_val, max_val):
    st.session_state.root = build_balanced_bst(min_val, max_val)
    st.session_state.current = st.session_state.root
    st.session_state.path = []
    st.session_state.questions = 0
    st.session_state.game_over = False
    st.session_state.inconsistent = False
    st.session_state.game_started = False
    st.session_state.last_range = (min_val, max_val)

# Main UI
st.title("🔢 Number Guessing Game")
st.markdown("---")

if not st.session_state.game_started:
    col_intro, _ = st.columns([2, 1])
    with col_intro:
        st.subheader("Welcome to the Binary Search Challenge!")
        st.markdown(f"### 🎯 Imagine a number between **{min_val}** and **{max_val}**.")
        st.write("I will try to find it by asking as few questions as possible using a Binary Search Tree.")
        if st.button("🚀 I'm Ready! Start Game"):
            st.session_state.game_started = True
            st.rerun()
    st.stop()

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("🏁 Game Controls")
    
    if not st.session_state.game_over and not st.session_state.inconsistent:
        current = st.session_state.current
        if current:
            st.metric("Questions Asked", st.session_state.questions)
            st.markdown(f"### Is your number higher, lower, or equal to **{current.value}**?")
            
            c1, c2, c3 = st.columns(3)
            # Higher Column (Left)
            if c1.button("⬆ Higher"):
                st.session_state.path.append(current.value)
                st.session_state.current = current.right
                st.session_state.questions += 1
                if not st.session_state.current:
                    st.session_state.inconsistent = True
                st.rerun()
                
            # Equal Column (Middle)
            if c2.button("✅ Equal"):
                st.session_state.path.append(current.value)
                st.session_state.game_over = True
                st.session_state.questions += 1
                st.rerun()
                
            # Lower Column (Right)
            if c3.button("⬇ Lower"):
                st.session_state.path.append(current.value)
                st.session_state.current = current.left
                st.session_state.questions += 1
                if not st.session_state.current:
                    st.session_state.inconsistent = True
                st.rerun()
        else:
            st.session_state.inconsistent = True
            st.rerun()

    elif st.session_state.game_over:
        st.success(f"### 🎯 Found it! Your number is **{st.session_state.path[-1]}**")
        st.balloons()
        if st.button("Play Again"):
            st.session_state.game_over = False
            st.session_state.root = build_balanced_bst(min_val, max_val)
            st.session_state.current = st.session_state.root
            st.session_state.path = []
            st.session_state.questions = 0
            st.session_state.game_started = False
            st.rerun()

    elif st.session_state.inconsistent:
        st.error("### ❌ Inconsistent answers detected.")
        st.warning("Logic suggests your number doesn't exist in the current range given your past answers.")
        if st.button("Restart"):
            st.session_state.inconsistent = False
            st.session_state.root = build_balanced_bst(min_val, max_val)
            st.session_state.current = st.session_state.root
            st.session_state.path = []
            st.session_state.questions = 0
            st.session_state.game_started = False
            st.rerun()

with col2:
    st.subheader("🌲 Decision Tree Visualization")
    current_val = st.session_state.current.value if st.session_state.current else None
    fig = render_tree_state(
        st.session_state.root, 
        st.session_state.path, 
        current_val,
        st.session_state.inconsistent
    )
    st.pyplot(fig)

