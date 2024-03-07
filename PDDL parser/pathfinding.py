#Manhattan distance used for heuristic
def h(cell1,cell2):
    x1, y1 = int(cell1[4]), int(cell1[5])
    x2, y2 = int(cell2[4]), int(cell2[5])

    return abs(x1-x2) + abs(y1-y2)

right_of = {
    'cell00': 'cell01', 'cell01': 'cell02', 'cell02': 'cell03', 'cell03': 'cell04',
    'cell10': 'cell11', 'cell11': 'cell12', 'cell12': 'cell13', 'cell13': 'cell14',
    'cell20': 'cell21', 'cell21': 'cell22', 'cell22': 'cell23', 'cell23': 'cell24',
    'cell30': 'cell31', 'cell31': 'cell32', 'cell32': 'cell33', 'cell33': 'cell34',
    'cell40': 'cell41', 'cell41': 'cell42', 'cell42': 'cell43', 'cell43': 'cell44'
}

left_of = {
    'cell01': 'cell00', 'cell02': 'cell01', 'cell03': 'cell02', 'cell04': 'cell03',
    'cell11': 'cell10', 'cell12': 'cell11', 'cell13': 'cell12', 'cell14': 'cell13',
    'cell21': 'cell20', 'cell22': 'cell21', 'cell23': 'cell22', 'cell24': 'cell23',
    'cell31': 'cell30', 'cell32': 'cell31', 'cell33': 'cell32', 'cell34': 'cell33',
    'cell41': 'cell40', 'cell42': 'cell41', 'cell43': 'cell42', 'cell44': 'cell43'
}

is_above = {
    'cell10': 'cell00', 'cell20': 'cell10', 'cell30': 'cell20', 'cell40': 'cell30',
    'cell11': 'cell01', 'cell21': 'cell11', 'cell31': 'cell21', 'cell41': 'cell31',
    'cell12': 'cell02', 'cell22': 'cell12', 'cell32': 'cell22', 'cell42': 'cell32',
    'cell13': 'cell03', 'cell23': 'cell13', 'cell33': 'cell23', 'cell43': 'cell33',
    'cell14': 'cell04', 'cell24': 'cell14', 'cell34': 'cell24', 'cell44': 'cell34'
}

is_underneath = {
    'cell00': 'cell10', 'cell10': 'cell20', 'cell20': 'cell30', 'cell30': 'cell40',
    'cell01': 'cell11', 'cell11': 'cell21', 'cell21': 'cell31', 'cell31': 'cell41',
    'cell02': 'cell12', 'cell12': 'cell22', 'cell22': 'cell32', 'cell32': 'cell42',
    'cell03': 'cell13', 'cell13': 'cell23', 'cell23': 'cell33', 'cell33': 'cell43',
    'cell04': 'cell14', 'cell14': 'cell24', 'cell24': 'cell34', 'cell34': 'cell44'
}

def validifyRight(cell1, cell2):
    return right_of.get(cell1) == cell2

def validifyLeft(cell1, cell2):
    return left_of.get(cell1) == cell2

def validifyUp(cell1, cell2):
    return is_above.get(cell1) == cell2

def validifyDown(cell1, cell2):
    return is_underneath.get(cell1) == cell2

def moveRight(cell):
    return right_of.get(cell)

def moveLeft(cell):
    return left_of.get(cell)

def moveUp(cell):
    return is_above.get(cell)

def moveDown(cell):
    return is_underneath.get(cell)

def generate_successors(current_cell):
    successors = []
    
    right_cell = moveRight(current_cell)
    if right_cell and validifyRight(current_cell, right_cell):
        successors.append(right_cell)

    left_cell = moveLeft(current_cell)
    if left_cell and validifyLeft(current_cell, left_cell):
        successors.append(left_cell)

    up_cell = moveUp(current_cell)
    if up_cell and validifyUp(current_cell, up_cell):
        successors.append(up_cell)

    down_cell = moveDown(current_cell)
    if down_cell and validifyDown(current_cell, down_cell):
        successors.append(down_cell)

    return successors