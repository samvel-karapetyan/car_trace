import streamlit as st


class Car:
    def __init__(self, max_line_number, line_number: int = 0):
        self.max_line_number = max_line_number
        if "car_position" not in st.session_state:
            st.session_state['car_position'] = line_number
        self.line_number = st.session_state['car_position']

    def up(self):
        """Implements turn up action."""
        if self.line_number != 0:
            self.line_number -= 1
            self.save()

    def down(self):
        """Implements turn down action."""
        if self.line_number != self.max_line_number:
            self.line_number += 1
            self.save()

    def save(self):
        st.session_state['car_position'] = self.line_number

    def get_position(self):
        return self.line_number