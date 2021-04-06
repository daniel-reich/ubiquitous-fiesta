
class Battleship:
    def __init__(self, scheme, guesses):
        self.ships = {('ABCDE'.index(s[0]), '12345'.index(s[1]))
                      for s in scheme}
        self.shots = {('ABCDE'.index(s[0]), '12345'.index(s[1]))
                      for s in guesses}
        self._hits = set()
        self.miss = set()
        for shot in self.shots:
            if shot in self.ships:
                self._hits.add(shot)
            else:
                self.miss.add(shot)
        rem_ships = self.ships - self._hits
        self.n_patrol, self.n_cruiser = 0, 0
        while rem_ships:
            ship_part = rem_ships.pop()
            neighbor = False
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                candidate = (ship_part[0] + i, ship_part[1] + j)
                if candidate in self.ships:
                    neighbor = True
                    if candidate in rem_ships:
                        rem_ships -= {candidate}
                    break
            if neighbor:
                self.n_cruiser += 1
            else:
                self.n_patrol += 1
​
    def board(self):
        b = [[' ' for col in range(5)] for row in range(5)]
        for r, c in self.ships:
            b[r][c] = 's'
        for r, c in self._hits:
            b[r][c] = 'X'
        for r, c in self.miss:
            b[r][c] = '.'
        return b
​
    def hits(self):
        return len(self._hits)
​
    def sunk(self):
        return 3 - self.n_cruiser
​
    def points(self):
        return len(self._hits) + 2 * (3 - self.n_cruiser)

