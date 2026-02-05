from src.line import Line # from src.line import Line


class Road:
    def __init__(self, 
            lines_count: int, 
            line_length: int,
            barrier_proportion: float,            
            ):
        self.lines_count = lines_count

        self.road = [
            Line(line_length=line_length, barrier_proportion=barrier_proportion) 
            for _ in range(self.lines_count)
        ]

    def move(self):
        for line in self.road:
            line.move()

    def get_road(self) -> list[str]: # hint
        return [line.get_line() for line in self.road]