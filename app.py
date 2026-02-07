from src.game import Game
import streamlit as st

def main():
    game = Game(
        line_length=10
    )

    game.run()
    # dict
    # cols = st.columns(6, gap=None) # list
    # for c in cols:
    #     c.image("assets/road.png")

if __name__ == "__main__":
    main()