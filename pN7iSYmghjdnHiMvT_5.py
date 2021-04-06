
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
    def __init__(self, scheme, guesses):
        self.scheme = scheme
        self.guesses = guesses
​
    def board(self):
        arr = [[str(c) + str(n) for n in range(1, 6)] for c in 'ABCDE']
        for i, row in enumerate(arr):
            for j, item in enumerate(row):
                if item in self.scheme and item in self.guesses:
                    arr[i][j] = 'X'
                elif item in self.scheme and item not in self.guesses:
                    arr[i][j] = 's'
                elif item not in self.scheme and item in self.guesses:
                    arr[i][j] = '.'
                else:
                    arr[i][j] = ' '
        return arr
​
    def hits(self):
        return sum(1 if i in self.scheme else 0 for i in self.guesses)
​
    def sunk(self):
        arr = [[1 if str(c) + str(n) in [item for item in self.guesses if item in self.scheme] else 0 for n in range(1, 6)] for c in 'ABCDE']
        return sum(sum([[(arr[i][j] * arr[i][j + 1] or arr[i][j] * arr[i + 1][j] or arr[i + 1][j + 1] * arr[i + 1][j] or arr[i + 1][j + 1] * arr[i][j + 1]) for i in range(4)] for j in range(4)], []))
​
    def points(self):
        return self.hits() + 2 * self.sunk()

