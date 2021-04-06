
def distance_to_nearest_vowel(txt):
    vov = ['a', 'e', 'i', 'o', 'u']
​
    distanceList = []
​
    for i, char in enumerate(txt):
        if(char in vov):
            distanceList.append(0)
            for j in range(i-1,-1,-1):
                if(0 not in distanceList[0:i]):
                    distanceList[j] = i-j
                else:
                    if(distanceList[j] > i-j):
                        distanceList[j] = i-j
        else:
            if(len(distanceList) == 0):
                distanceList.append(1)
            else:
                distanceList.append(distanceList[-1] + 1)
​
    return distanceList

