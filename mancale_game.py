class Mancala:
    def __init__(self, hole: int, seeds: int):
        self.seeds = seeds
        self.hole = [seeds] * hole + [0] + [seeds] * hole + [0]  # 2 rows + 2 stores
        self.current_player = 1

    def status(self):
        return tuple(self.hole)

    def play(self, hole):
        if hole < 0 or hole >= len(self.hole):
            raise IndexError("Hole number is out of range.")
        if self.hole[hole] == 0:
            raise ValueError("Cannot play from an empty hole.")

        seeds = self.hole[hole]
        self.hole[hole] = 0
        idx = hole

        # Distributing seeds
        while seeds > 0:
            idx = (idx + 1) % len(self.hole)
            self.hole[idx] += 1
            seeds -= 1
