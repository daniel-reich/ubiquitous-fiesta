
def backtracking_stairs(cur, list_to_permutation, result_of_stairs, target):
    if sum(cur) == target:
        result_of_stairs.append(list(cur[:]))
    if sum(cur) > target:
        return
    for i in range(0, len(list_to_permutation)):
        cur.append(list_to_permutation[i])
        backtracking_stairs(cur, list_to_permutation, result_of_stairs, target)
        cur.pop()
    return result_of_stairs
​
def ways_to_climb(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a+b
    return a
​
def num_ways(n, s):
    if s == {1, 2}:
        return ways_to_climb(n)
    return len(backtracking_stairs([], list(s), [], n))

