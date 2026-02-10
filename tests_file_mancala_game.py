from mancale_game import Mancala


def test_initial_status():
    mancala1 = Mancala(6, 4)
    assert mancala1.initial_status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)


def test_illigal_hole():
    mancala1 = Mancala(6, 4)
    assert mancala1.play(5) is not IndexError
