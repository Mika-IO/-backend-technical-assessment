from itertools import product

def validate_coordinate(coordinate):
    """
        Return True if coordinate is valid, else return False
    """
    if len(coordinate) != 2:
        return False
    valid_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
    if not coordinate[0] in valid_letters:
        return False
    if not coordinate[1] in valid_numbers:
        return False
    return True

def future_knight_positions(coordinate):
    """
        Return a array with future positions of knight in 1 turn
    """
    if not validate_coordinate(coordinate):
        raise Exception('Invalid coordinate')
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]    
    x, y = letters.index(coordinate[0]), numbers.index(coordinate[1])
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
    positions = []
    for move in moves:
        positions.append(letters[move[0]] + numbers[move[1]])
    return positions

def future_knight_positions_in_two_turns(coordinate):
    """
        Return a turple with 2 array with future positions of knight in 2 turns
    """
    if not validate_coordinate(coordinate):
        raise ValueError('Invalid coordinate')
    first_turn = future_knight_positions(coordinate)
    second_turn = []
    for position in first_turn:
        second_turn = second_turn + future_knight_positions(position)
    return first_turn, second_turn
