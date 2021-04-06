
def min_palindrome_steps(txt):
    if len(txt) < 2 or list(txt) == list(reversed(txt)): return 0
    count = 0
    return [len(i) for i in list(reversed([''.join(list(reversed(txt)))[i:] for i in range(len(txt))])) if list(txt+i) == list(reversed(txt+i))][0]

