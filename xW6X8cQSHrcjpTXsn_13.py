
def first_and_last(s):
    return ["".join(sorted([i for i in s])), "".join(sorted([i for i in s], reverse=True))]

