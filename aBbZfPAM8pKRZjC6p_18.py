
def fruit_salad(fruits):
    temp = []
    for i in fruits:
        l = len(i)
        temp.append(i[:l//2])
        temp.append(i[l//2:])
    temp = sorted(temp)
    return ''.join(temp)

