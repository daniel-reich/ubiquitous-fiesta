
def circular_shift(lst1,lst2,num):
    rotate = []
    if lst1 == lst2:
        return True
    if num > 0:
        for i in range(0,len(lst1)):        # take lst2 and rotate it with num
            rotate.append(lst2[i-num])
    if num < 0:
        for i in range(0,len(lst1)):        # take lst2 and rotate it with num
            rotate.append(lst2[i+num])
    if lst1 == rotate:                  # if lst1 is equal to lst2 rotated, then we know that lst2 is the num rotated version of lst1
        return True
    else:
        return False

