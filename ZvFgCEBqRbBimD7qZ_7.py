
def bowling(array):
    i = 0
    score = 0
    while i < len(array):
        try:
            if array[i] == 10:
                score = score + array[i]+array[i+1]+array[i+2]
                i+=1
            elif array[i]+array[i+1] == 10:
                score = score + array[i]+array[i+1]+array[i+2]
                i+=2
            else:
                score = score + array[i]+array[i+1]
                i+=2
        except:
            return score
    return score

