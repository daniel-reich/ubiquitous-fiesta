
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
​
    def __init__(self, scheme, guesses):
        '''
        Sets up board, placement of ships player's guesses & scores
        '''
        self._board = [[' '] * 5 for _ in range(5)]  # initial board
        self._hits = self._sunk = self._points = 0
        convert = lambda x: (ord(x[0]) - ord('A'), int(x[1]) - 1)
​
        # Update board with scheme and guess hits
        guesses_copy = guesses[:]   # guesses gets reused in the tests!!!
        for loc in scheme:
            row, col = convert(loc)
            if loc in guesses:
                self._hits += 1
                self._board[row][col] = 'X'
                guesses_copy.remove(loc)
            else:
                self._board[row][col] = 's'
​
        # Record misses
        for guess in guesses_copy:
            row, col = convert(guess)
            self._board[row][col] = '.'
​
        # Record sunk Cruisers
        self._sunk += sum(1 if row[i] + row[i+1] == 'XX' else 0 # rows
                          for row in self._board for i in range(4))
        self._sunk += sum(1 if col[i] + col[i+1] == 'XX' else 0 # columns
                          for col in zip(*self._board) for i in range(4))
​
    def board(self):
        return self._board
​
    def hits(self):
        return self._hits
​
    def sunk(self):
        return self._sunk
​
    def points(self):
        return self._hits + 2 * self._sunk

