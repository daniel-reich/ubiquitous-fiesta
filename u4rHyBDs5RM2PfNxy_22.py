
def count_ones(lst):
    cnt=0
    if lst[0]==1 and lst[1]==1:
        cnt += 1
    for i in range (len(lst)-2):
        if lst[i]==0 and lst[i+1]==1 and lst[i+2]==1:
            cnt +=1
    return cnt

