class Mancala:
    def __init__(self, hole: int, seeds: int):
        self.seeds = seeds
        self.hole = [seeds] * hole + [0] + [seeds] * hole + [0]  # 2 rows + 2 stores
        self.current_player = 1

    def initial_status(self):
        return tuple(self.hole)

    def play(self, hole):
        if hole < 0 or hole >= len(self.hole):
            raise IndexError("Hole number is out of range.")
