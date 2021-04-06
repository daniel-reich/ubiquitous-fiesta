
def calculate_scores(txt):
    count = 0
    count1 = 0
    count2 = 0
    for char in txt:
        if (char=='A'): 
            count += 1
        elif (char=='B'):
            count1 += 1
        else:
            count2 += 1
    return [count,count1,count2]

