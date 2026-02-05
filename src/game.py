import streamlit as st
from src.car import Car
from src.road import Road
import time


class Game:
    def __init__(
            self,
            lines_count: int = 3, 
            line_length: int = 20,
            barrier_proportion: float = 0.1,            
            line_number: int = 0
            ):
        self.road = Road(
            lines_count=lines_count,
            line_length=line_length,
            barrier_proportion=barrier_proportion
        )

        self.car = Car(
            max_line_number=lines_count - 1,
            line_number=line_number
        )

        self.st_containers = [st.empty() for _ in range(lines_count)]

    def draw(self):
        current_road = self.road.get_road()

        for line, st_container in zip(current_road, self.st_containers):
            st_container.write(line)

    def run(self):
        # for _ in range(20):
        while True:
            self.draw() # draw the current state 
            self.road.move()

            time.sleep(0.1)