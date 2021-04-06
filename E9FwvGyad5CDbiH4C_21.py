
def block(lst):
    count=0
    for i in range(len(lst[0])):
        for j in range(len(lst)-1):
            if lst[j][i]>lst[j+1][i]:
                count=count+len(lst)-j-1
    return count

