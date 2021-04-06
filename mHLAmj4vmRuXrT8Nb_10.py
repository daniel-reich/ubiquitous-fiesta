
def consecutive_combo(lst1, lst2):
    combined = lst1 + lst2
    for i in range(min(combined), max(combined) + 1):
        if i not in combined:
            return False
    return True

