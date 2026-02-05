class Car:
    def __init__(self, max_line_number, line_number: int = 0):
        self.max_line_number = max_line_number
        self.line_number = line_number

    def up(self):
        """Implements turn up action."""
        if self.line_number != 0:
            self.line_number -= 1

    def down(self):
        """Implements turn down action."""
        if self.line_number != self.max_line_number:
            self.line_number += 1