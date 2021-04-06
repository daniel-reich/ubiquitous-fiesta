
def check_pattern(lst, pattern):
    if len(lst) != len(pattern):
        return False
    if len([i for i in lst if i == lst[0]]) == len(lst):
        if len([i for i in pattern if i == pattern[0]]) != len(pattern):
            return False
    visited = []
    for i in range(len(pattern)):
        pi = pattern[i]
        if pi not in visited:
            visited.append(pi)
        else:
            if lst[visited.index(pi)] != lst[i]:
                return False
            else:
                visited.append(pi) 
    return True

