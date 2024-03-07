#Manhattan distance used for heuristic
def h(cell1,cell2):
    x1, y1 = int(cell1[4]), int(cell1[5])
    x2, y2 = int(cell2[4]), int(cell2[5])

    return abs(x1-x2) + abs(y1-y2)