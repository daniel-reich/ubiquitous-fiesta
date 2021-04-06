
def identify(*cube):
    lst = [len(row) for row in cube]
    max_row = max(lst)
    missing = sum(max_row - r for r in lst)
    return ("Full" if len(lst) == max_row and missing == 0 else
            "Missing {}".format(missing) if missing else "Non-Full")

