import streamlit as st
import time

st.title("Simple Animation")

if "x" not in st.session_state:
    st.session_state.x = 0

canvas = st.empty()

if not st.button("Start"):
    for i in range(20):
        st.session_state.x = i
        canvas.write(
            f"{i*'S'}🚗",
            unsafe_allow_html=True
        )
        time.sleep(0.1)

# Line -> - - X - - - - - - - - - - - - - - -

#  - - X - - - - - - - - - - - - - - -               # 0
# 🚗 - - - - - - - X - - - - - - - -X X -          # 1
#  - - - - - - - - - - - - - - - - - X -             # 2

# <-, ->