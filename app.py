from src.game import Game
import streamlit as st


def main():
    game = Game(
        line_length=50
    )

    game.run()    


if __name__ == "__main__":
    main()