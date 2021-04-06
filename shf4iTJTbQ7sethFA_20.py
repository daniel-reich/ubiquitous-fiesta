
def magic_square_game(alice, bob):
    check = 0
    suma = 0
    sumb = 0
​
    for i in range(0, len(alice[1])):
        suma = suma + int(alice[1][i])
​
    if suma%2 != 1:
        check = 1
​
    for i in range(0, len(bob[1])):
        sumb = sumb + int(bob[1][i])
​
    if sumb%2 != 0:
        check = 1
​
    if alice[1][bob[0]-1] != bob[1][alice[0]-1]:
        check = 1
​
    if check == 1:
        return False
    else:
        return True

