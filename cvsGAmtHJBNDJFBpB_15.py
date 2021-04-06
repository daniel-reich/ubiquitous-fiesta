
def can_traverse(boxes):
    '''
    Rturns True if it is possible to traverse from left to right by climbing up
    or jumping down 1 box at a time as per the rules above.
    '''
    box_totals = [[sum(boxes[i][j] for i in range(len(boxes)))][0] for j in range(len(boxes[0]))]
    return all(abs(b - a) <= 1 for a, b in zip(box_totals, box_totals[1:]))

