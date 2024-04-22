from symbols import W, G, E, L


# this function just takes the level number and returns the map object for that level
def get_map(level):
    if level == 1:
        return level_one
    if level == 2:
        return level_two


# a move is valid if the new space:
# (1) is within the bounds of the map spaces
# (2) is not a wall
def is_valid_move(position, map):
    if position[0] < 0 or position[0] >= len(map):
        return False
    if position[1] < 0 or position[1] >= len(map[0]):
        return False
    if map[position[0]][position[1]] == W:
        return False
    return True


level_one = [
    [W, W, W, W, W, W, W, W, W, W],
    [W, E, E, W, E, E, G, W, E, W],
    [W, E, E, W, E, E, E, E, W, W],
    [W, G, E, E, E, E, E, E, W, W],
    [W, E, E, E, E, E, E, E, W, W],
    [W, E, W, W, W, W, E, E, W, W],
    [W, E, E, E, E, G, E, E, W, W],
    [W, E, E, E, E, E, E, E, E, W],
    [W, E, E, E, E, W, E, W, E, W],
    [W, E, E, W, E, W, E, W, E, W],
    [W, E, E, E, E, W, E, W, E, W],
    [W, E, E, E, E, W, E, W, E, W],
    [W, E, E, E, E, W, L, W, G, W],
    [W, W, W, W, W, W, W, W, W, W]
]

level_two = [
    [W, W, W, W, W, W, W, W, W, W],
    [W, E, E, W, E, E, G, W, E, W],
    [W, E, E, W, E, E, E, E, W, W],
    [W, E, E, E, E, E, E, E, W, W],
    [W, E, E, E, E, E, W, E, W, W],
    [W, E, W, E, E, W, E, E, W, W],
    [W, E, E, E, E, E, E, E, W, W],
    [W, E, E, G, E, E, E, E, E, W],
    [W, E, E, E, E, W, E, W, E, W],
    [W, E, E, W, E, W, E, W, E, W],
    [W, E, E, E, E, W, G, W, E, W],
    [W, E, E, E, E, W, E, W, E, W],
    [W, E, E, E, E, W, E, W, W, W],
    [W, W, W, W, W, W, W, W, W, W]
]