
def chess_board(pole):
    x = int(''.join([i for i in pole if i.isdigit()]))
    y = ''.join([i for i in pole if i.isalpha()])
    return 'black' if (ord(y) % 2 == 1 and x % 2 == 1) or (ord(y) % 2 == 0 and x % 2 == 0) else 'white'

