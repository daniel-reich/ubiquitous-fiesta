
def generate_permutation(cur, n, result_of_permutation):
    if len(cur) == n:
        result_of_permutation.append(cur[:])
        # use deepcopy because curr is tracking all partial solution, it eventually become []
        # !!! VERY VERY VERY IMPORTANT
    for i in '01':
        if len(cur[:]) == n:
            continue
        elif len(cur[:]) != 0 and cur[:][-1] == "1":
            cur.append("0")
        else:
            cur.append(i)
​
        # move to the next solution
        generate_permutation(cur, n, result_of_permutation)
        # backtrack (the most important part, soul of the backtracking)
        # backtrack to previous partial state
        cur.pop()
    return result_of_permutation
​
def generate_nonconsecutive(n):
    result = []
    for item in generate_permutation([], n, []):
        result.append(''.join(item))
    return ' '.join(sorted(list(set(result))))

