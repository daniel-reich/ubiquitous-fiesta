
def josephus(people):
    prisoners = []
    for x in range(people):
        prisoners.append(str(x+1))
    count = 1
    while len(prisoners)>1:
        if count>=len(prisoners):
            count -= len(prisoners)
            continue
        prisoners.pop(count)
        count += 1
    return int(prisoners[0])

