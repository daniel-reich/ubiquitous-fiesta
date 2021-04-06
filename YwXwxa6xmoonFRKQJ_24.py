
def josephus(n):
    prisoners = []
    if n == 0:
        return False
    for x in range(n):
        prisoners.append(str(x))
    count = 1
    while len(prisoners)>1:
        if count>=len(prisoners):
            count -= len(prisoners)
            continue
        prisoners.pop(count)
        count += 1
    return int(prisoners[0])

