
def min_swaps(s1, s2):
    counter = 0
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            counter = counter+1
            
    return int(counter / 2)

