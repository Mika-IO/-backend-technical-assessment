import pytest
from chesschallenge.chess.chess import future_knight_positions
from chesschallenge.chess.chess import future_knight_positions_in_two_turns

def test_d4_future_knight_positions():
    result = ['c2', 'c6', 'e2', 'e6', 'b3', 'b5', 'f3', 'f5']
    assert future_knight_positions("d4") == result

def test_a1_future_knight_positions_in_two_turns():
    result = (['b3', 'c2'], ['a1', 'a5', 'c1', 'c5', 'd2', 'd4', 'b4', 'd4', 'a1', 'a3', 'e1', 'e3'])
    assert future_knight_positions_in_two_turns("a1") == result

def test_z3_future_knight_positions_in_two_turns():
    with pytest.raises(ValueError):
        future_knight_positions_in_two_turns("z3")
