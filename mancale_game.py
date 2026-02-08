from random import seed


class Mancala:
    def __init__(self, hole: int, seeds: int):
        self.hole = hole
        self.seeds = seeds
        self.stores = 0

    def initial_status(self):
        pits = (self.seeds,) * self.hole
        return (
            *pits,
            0,
        ) * 2
