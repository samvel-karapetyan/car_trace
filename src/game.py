import streamlit as st
from src.car import Car
from src.road import Road
import time
import os


class Game:
    def __init__(
            self,
            lines_count: int = 3, 
            line_length: int = 10,
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

        self.road_path = os.path.join("assets", "road.png")
        self.bbq_path = os.path.join("assets", "bbq.png")
        self.car_path = os.path.join("assets", "car.png")

        self.st_containers = [st.empty() for _ in range(lines_count)]
        
        if "current_score" not in st.session_state:
            st.session_state['current_score'] = 0

    def draw(self):
        current_road = self.road.get_road()
        # [[0, 0, 0, 1, 1, 1, 0, 0, ], [0, 1, 0, 0, 1, 1], ... ]
        car_position = self.car.get_position() # 0|1|2

        # enumerate
        # for a in it:
        #   ...
        
        # for i, a in enumerate(it):
        #   ...

        # for i in range(len(line)): line = current_road[i], st_container=self.st_containers[i]

        for i, (line, st_container) in enumerate(zip(current_road, self.st_containers)):
            # line = [0, 0, 0, 1, 1, 1, 0, 0]
            # st_container.write(...)
            cols = st_container.columns(len(line), gap=None)
            for j, (state, col) in enumerate(zip(line, cols)):
                if i == car_position and j == 0:
                    col.image(self.car_path)
                    continue

                # col.write(str((i, j)))
                col.image(self.road_path if state == 0 else self.bbq_path)

    def check_crash(self) -> bool:
        current_road = self.road.get_road()
        car_position = self.car.get_position()

        return current_road[car_position][0] == 1

    def run(self):
        up, down = st.columns(2)
        up_pressed = up.button("Up", shortcut="Up")
        down_pressed = down.button("Down", shortcut="Down")

        if up_pressed:
            self.car.up()

        if down_pressed:
            self.car.down()

        # 0.5 -> 0.1
        # 20s

        # 0.1 * t + 0.5 * (1 - t)

        if "start" not in st.session_state:
            st.session_state['start'] = time.perf_counter()
        start = st.session_state['start']

        while True:
            self.draw() # draw the current state 
            self.road.move()

            st.session_state['current_score'] += 1

            if self.check_crash():
                st.header(f"Loooooser! Your Score is: {st.session_state['current_score']}")
                break

            curr_time = time.perf_counter()
            diff = curr_time - start

            if diff > 20:
                delay = 0.1
            else:
                diff_normalized = diff / 20
                delay = 0.1 * diff_normalized + 0.5 * (1 - diff_normalized)

            time.sleep(delay)