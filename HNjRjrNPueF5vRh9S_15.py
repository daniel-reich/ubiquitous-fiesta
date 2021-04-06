
def hamming_code(message):
    temp = []
    for i in message:
        temp.append(ord(i))
​
    for i in range(len(temp)):
        temp[i] = bin(temp[i])[2:].zfill(8)
​
    for i in range(len(temp)):
        temp2 = ''
        for j in range(len(temp[i])):
            temp2 += 3*temp[i][j]
        temp[i] = temp2
​
​
    return ''.join(temp)

