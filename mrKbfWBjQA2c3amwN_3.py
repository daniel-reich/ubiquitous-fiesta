
def mult_table(n):
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append((i+1)*(j+1))
    return result

