
def num_split(num):
    if num < 0:
        return [int('-' + str(int(j)*10**int(len(str(num))-(i+2)))) for i,j in enumerate(str(abs(num)))]
    return [int(j)*10**int(len(str(num))-(i+1)) for i,j in enumerate(str(num))]

