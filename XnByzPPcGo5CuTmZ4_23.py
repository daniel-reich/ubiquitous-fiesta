
def kix_code(addr):
​
    for i in range(len(addr)):
        if addr[i].isdigit():
            a = i
            break
    temp = addr[a:]
    temp = temp.split(',')
​
    t = ''
    for i in range(len(temp[0])):
        if temp[0][i].isdigit() or temp[0][i].isalpha():
            t += temp[0][i].upper()
        else:
            t += 'X'
    temp[0] = t
    temp[1] = temp[1].split(' ')
​
    return temp[1][1] + temp[1][2] + temp[0]

