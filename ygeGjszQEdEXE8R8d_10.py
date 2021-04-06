
def move(mat):
    matrix = [row.copy() for row in mat]
​
    def up():
        matrix.append(matrix.pop(0))
​
    def down():
        matrix.insert(0, matrix.pop())
​
    def right():
        for row in matrix:
            row.insert(0, row.pop())
​
    def left():
        for row in matrix:
            row.append(row.pop(0))
​
    actions = {
        "up": up,
        "down": down,
        "left": left,
        "right": right
    }
​
    def mover(action: str):
        action = action.casefold()
        if action == "stop":
            return matrix
​
        actions[action]()
        return mover
​
    return mover

