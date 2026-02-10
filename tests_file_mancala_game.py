from mancale_game import Mancala


def test_initial_status():
    mancala1 = Mancala(6, 4)
    assert mancala1.status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)


def test_illegal_hole():
    mancala1 = Mancala(6, 4)
    assert mancala1.play(5) is not IndexError


def test_simple_move():
    mancala1 = Mancala(6, 4)
    mancala1.play(0)  # Player 1 plays from hole 0
    assert mancala1.status() == (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0)
    mancala2 = Mancala(6, 4)
    mancala2.play(1)  # Player 1 plays from hole 1
    assert mancala2.status() == (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0)
