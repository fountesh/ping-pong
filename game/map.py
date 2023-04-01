import pygame
map = [
    ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"],
    ["_", "_", "_", "A", "_", "_", "_", "_", "_", "A", "A", "A"],
    ["_", "_", "_", "A", "_", "_", "_", "_", "_", "A", "A", "A"],
    ["A", "_", "_", "A", "_", "_", "A", "_", "_", "_", "A", "A"],
    ["A", "_", "_", "A", "_", "_", "A", "_", "_", "_", "_", "A"],
    ["A", "_", "_", "A", "_", "_", "A", "_", "_", "_", "_", "A"],
    ["A", "_", "_", "A", "_", "_", "A", "_", "_", "_", "_", "A"],
    ["A", "_", "_", "A", "_", "_", "A", "_", "_", "_", "_", "A"],
    ["A", "_", "_", "_", "_", "_", "A", "_", "_", "_", "_", "A"],
    ["A", "_", "_", "_", "_", "_", "A", "_", "_", "_", "_", "A"],
    ["A", "_", "_", "_", "_", "_", "A", "_", "_", "_", "_", "A"],
    ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"],
]
SIZE = 600 / 12
def make_map():
    result = []
    for row in range(len(map)):
        for column in range(len(map[row])):
            if map[row][column] == "A":
                x = SIZE * (column + 2)
                y = SIZE * row
                result.append(pygame.Rect(x, y, SIZE, SIZE))
    return result

make_map()