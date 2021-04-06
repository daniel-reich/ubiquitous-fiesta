
def can_move(chess, start, end):
    dictionary = {'A':1, 'B': 2, 'C':3, 'D':4, 'E':5, 'F': 6, 'G':7, 'H':8, }
    if chess == "Rook":
        if start[0] == end[0] or start[1] == end[1]:
            return True
        else: 
            return False
    if chess == "Bishop":
        if abs(dictionary[start[0]] - dictionary[end[0]]) == abs(int(start[1]) - int(end[1])):
            return True
        else:
            return False
    if chess == "Knight":
        if abs(dictionary[start[0]] - dictionary[end[0]]) == 1:
            if abs(int(start[1]) - int(end[1])) == 2:
                return True
            else:
                return False
        if abs(dictionary[start[0]] - dictionary[end[0]]) == 2:
            if abs(int(start[1]) - int(end[1])) == 1:
                return True
            else:
                return False
        else:
            return False
    if chess == "Queen":
        if start[0] == end[0] or start[1] == end[1]:
            return True
        if abs(dictionary[start[0]] - dictionary[end[0]]) == abs(int(start[1]) - int(end[1])):
            return True
        else:
            return False
    if chess == "King":
        if abs(dictionary[start[0]] - dictionary[end[0]]) == 1 or abs(int(start[1]) - int(end[1])) == 1:
            return True
        else:
            return False
        
    if chess == "Pawn":
        if start[0] == end[0]:
            if int(end[1]) - int(start[1]) == 1 or int(end[1]) - int(start[1]) == 2:
                return True
            else:
                return False
        else:
            return False

