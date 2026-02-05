import random


class Line:
    def __init__(self, line_length: int = 20, barrier_proportion: float = 0.1):
        self.line_length = line_length
        self.barrier_proportion = barrier_proportion

        self.symbols = ['O', 'X']
        self.weights = [1 - self.barrier_proportion, self.barrier_proportion]
        
        self.line = self.generate_line()

    def generate_line(self):
        # -, X -> self.line_length
        # random.choice - choose one random element from "list"
        line = 5 * [self.symbols[0]]
        line += random.choices( # list.extend
            self.symbols, 
            weights=self.weights, 
            k=self.line_length - 5
        )

        return line
    
    def move(self):
        next_symbol = random.choices(
            self.symbols, 
            weights=self.weights,
            k=1
            )
        
        self.line = self.line[1:] + next_symbol

    def get_line(self):
        return " ".join(self.line)