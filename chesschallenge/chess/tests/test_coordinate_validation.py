import pytest
from chesschallenge.chess.chess import validate_coordinate


def test_a2_is_valid_coordenate():
    assert validate_coordinate("a2") == True

def test_c5_is_valid_coordenate():
    assert validate_coordinate("c5") == True

def test_34_is_valid_coordenate():
    assert validate_coordinate("34") == False

def test_345_is_valid_coordenate():
    assert validate_coordinate("345") == False

def test_ans_is_valid_coordenate():
    assert validate_coordinate("ans") == False

def test_bb_is_valid_coordenate():
    assert validate_coordinate("bb") == False

def test_z9_is_valid_coordenate():
    assert validate_coordinate("z9") == False