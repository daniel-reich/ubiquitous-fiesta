
def reorder_digits(lst, direction):
    if direction == "asc":
        return [int("".join(sorted(list(str(i))))) for i in lst]
    else:
        return [int("".join(sorted(list(str(i)), reverse=True))) for i in lst]

