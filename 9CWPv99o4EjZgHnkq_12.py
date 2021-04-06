
def divide(lst, n):
    temp = []
    chunks = []
    index = 0
    for i in lst:
        index += 1
        if index == len(lst):
            if sum(temp) + i <= n:
                temp.append(i)
                chunks.append(temp)
            else:
                chunks.append(temp)
                temp = []
                temp.append(i)
                chunks.append(temp)
        elif i + sum(temp) <= n:
            temp.append(i)
        else:
            chunks.append(temp)
            temp = []
            temp.append(i)
    return chunks

