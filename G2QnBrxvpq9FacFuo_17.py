
def possible_path(lst):
    in_hallway = True
    for eachnumber in lst:
        if str(eachnumber).isdigit() and in_hallway:
            in_hallway = False
        elif str(eachnumber).isdigit() and not in_hallway:
            return False
        elif eachnumber == 'H' and not in_hallway:
            in_hallway = True
    return True

