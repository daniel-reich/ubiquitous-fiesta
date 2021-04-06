
def swap(a,b):
    a,b=b,a
   
def number_of_swaps(lst):
    count=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                swap(lst[i],lst[j])
                count=count+1
    return count

