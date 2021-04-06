
def magic_square_game(alice, bob):
    if alice[1][bob[0]-1]==bob[1][alice[0]-1]:
        if (int(bob[1])==11 or int(bob[1])==101 or int(bob[1])==110) and (int(alice[1])!=11 and int(alice[1])!=101 and int(alice[1])!=110):
            return True
    return False

