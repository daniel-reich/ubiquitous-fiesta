
from string import ascii_uppercase
​
char_to_num = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=1)}
​
class Battleship(object):
​
    def __init__(self, scheme, guesses):
        self.scheme = []
        for string in scheme:
            self.scheme.append(str(int(char_to_num[string[0]]) - 1) + str(int(string[1]) - 1))
        self.guesses = []
        for string in guesses:
            self.guesses.append(str(int(char_to_num[string[0]]) - 1) + str(int(string[1]) - 1))
        self.hit_num = 0
        self.point_num = 0
        self.cruisers = []
        self.game_board = [[" "," "," "," "," "],
                           [" "," "," "," "," "],
                           [" "," "," "," "," "],
                           [" "," "," "," "," "],
                           [" "," "," "," "," "]]
        for cord in self.scheme:
            if (cord[0] + str(int(cord[1]) + 1)) in self.scheme:
                self.cruisers.append([cord, cord[0] + str(int(cord[1]) + 1)])
            elif (str(int(cord[0]) + 1) + cord[1]) in self.scheme:
                self.cruisers.append([cord, str(int(cord[0]) + 1) + cord[1]])
​
    def board(self):
        for row in range(0, len(self.game_board)):
            for cell in range(0, len(self.game_board[row])):
                if str(row)+str(cell) in self.scheme:
                    self.game_board[row][cell] = "s"
​
                if str(row)+str(cell) in self.guesses and str(row)+str(cell) in self.scheme:
                    self.game_board[row][cell] = "X"
​
                elif str(row)+str(cell) in self.guesses and not str(row)+str(cell) in self.scheme:
                    self.game_board[row][cell] = "."
​
        return self.game_board
​
    def hits(self):
        for row in self.game_board:
            self.hit_num += row.count("X")
        return self.hit_num
​
    def sunk(self):
        self.cruiser_sunk = 0
        for cruiser in self.cruisers:
            if cruiser[0] in self.guesses and cruiser[1] in self.guesses:
                self.cruiser_sunk += 1
        return self.cruiser_sunk
​
    def points(self):
        return (self.hit_num + (self.cruiser_sunk * 2))

