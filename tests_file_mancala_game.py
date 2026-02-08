def test_initial_status():
    mancala1 = Mancala(6, 4)
    assert mancala1.initial_status() == (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)
