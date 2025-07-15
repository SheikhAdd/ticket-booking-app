class Hall:
    ROWS = 5
    SEATS_PER_ROW = 10

    def __init__(self, hall_state=None):
        self.hall_state = hall_state if hall_state else {str(row): [] for row in range(1, self.ROWS + 1)}

    def is_seat_available(self, row, seat):
        return str(row) in self.hall_state and seat not in self.hall_state[str(row)]

    def book_seat(self, row, seat):
        if self.is_seat_available(row, seat):
            self.hall_state[str(row)].append(seat)
            return True
        return False

    def display(self):
        print("\nСхема зала:")
        for row in range(1, self.ROWS + 1):
            row_str = f"Ряд {row}: "
            for seat in range(1, self.SEATS_PER_ROW + 1):
                mark = "[X]" if seat in self.hall_state[str(row)] else "[ ]"
                row_str += f"{mark} "
            print(row_str)
        print()
