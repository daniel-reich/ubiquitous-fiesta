
def does_brick_fit(a,b,c, w,h):
    list1 = [a, b, c]
    list2 = [w, h]
    list1.remove(max(list1))
    if min(list1) <= min(list2) and max(list1) <= max(list2):
        return True
    else:
        return False

