
def ranged_reversal(lst, start, finish):
    zero = None if start == 0 else start - 1
    return lst[:start] + lst[finish:zero:-1] + lst[finish + 1:]

