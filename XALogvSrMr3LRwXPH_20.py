
def is_shuffled_well(a):
    for i in range(2,len(a)):
        if (a[i-1] == a[i]-1 and a[i-2] == a[i]-2) or (a[i-1] == a[i]+1 and a[i-2] == a[i]+2):
            return False
    return True

