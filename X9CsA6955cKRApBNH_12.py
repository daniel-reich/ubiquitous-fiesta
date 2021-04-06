
def longest_run(lst):
    result, current = 1, 1
    for i in range(len(lst) - 1):
        if lst[i+1] - lst[i] == 1:
            current += 1
            if current > result:
                result = current
        if lst[i+1] - lst[i] != 1:
            current = 1
    for i in range(len(lst) - 1):
        if lst[i+1] - lst[i] == -1:
            current += 1
            if current > result:
                result = current
        if lst[i+1] - lst[i] != -1:
            current = 1
    return result

