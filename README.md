# 🎯 Number Guessing Game (Binary Decision Tree)

A "premium" AI-powered number guessing game built using Python and Streamlit. The system uses a pre-built **Balanced Binary Decision Tree** to identify a number you're thinking of in the minimum number of steps.

## 🌟 Features

- **Balanced BST Logic**: Guaranteed to find any number in $O(\log N)$ questions (e.g., 7 steps for 1-100).
- **Real-time Visualization**: Watch the algorithm traverse the decision tree live as you provide answers.
- **Premium UI/UX**: Professional layout with color-coded controls and high-contrast styling.
- **Dynamic Configuration**: Customize the search range (e.g., 1-50, 1-1000) directly from the sidebar.
- **Consistency Check**: Detects if your answers lead to a logical impossibility.
- **Modular Codebase**: Clean separation of tree logic, game flow, and visualization.

## 🛠 Tech Stack

- **Python 3.x**
- **Streamlit**: For the interactive web interface.
- **NetworkX**: For graph/tree data structures.
- **Matplotlib**: For rendering the tree visualization.

## 📂 Project Structure

```text
├── streamlit_app.py        # Main entry point for the web app
├── main.py                 # CLI version of the game
├── tree.py                 # BST construction logic & Node class
├── game.py                 # Modular game traversal logic
├── visualize_streamlit.py  # Real-time tree rendering logic
├── utils.py                # Helper functions (input validation)
└── requirements.txt        # Project dependencies
```

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the required packages:
```bash
pip install -r requirements.txt
```

### 2. Running the Web Game (Recommended)
Launch the interactive Streamlit application:
```bash
streamlit run streamlit_app.py
```

### 3. Running the CLI Version
Play the game directly in your terminal:
```bash
python main.py
```

## 📚 Logic Explanation

### Tree Construction
The system builds a balanced binary search tree by recursively selecting the **median** of the current range as the pivot. This ensures that each question asked by the AI eliminates **50%** of the remaining search space.

### Complexity
For a range of size $N$, the maximum number of questions is:
$$\text{Steps} = \lceil \log_2(N) \rceil$$

---
*Created as part of a Senior Software Engineering challenge.*
