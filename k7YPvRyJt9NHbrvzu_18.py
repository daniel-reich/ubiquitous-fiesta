
def football_score_backtracking(cur, lst, result, target, index):
    if sum(cur) == target:
        result.append(cur[:])
    if sum(cur) > target:
        return
    else:
        for i in range(index, len(lst)):
              cur.append(lst[i])
              football_score_backtracking(cur, lst, result, target, i)
              cur.pop()
    return result
​
def football(score):
    return len(football_score_backtracking([], [2, 3, 6, 7, 8], [], score, 0))

