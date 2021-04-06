
def simon_says(lst1, lst2):
    for n in range(len(lst1)):
        if lst1[n]==lst2[n+1]:
            return True
        else:
            return False

