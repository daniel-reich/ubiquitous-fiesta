
def find_index(lst, str):
    for i, x in enumerate(lst):
        if x == str:
            break
    return i

