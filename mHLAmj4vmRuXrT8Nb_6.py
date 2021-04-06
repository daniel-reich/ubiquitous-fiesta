
def consecutive_combo(lst1, lst2):
    a = sorted(lst1+lst2)
    for i in range(len(a)):
        if (sum(a))/(len(a)) == ((a[i] + a[len(a)-1])/2):
            return True
        else:
            return False

