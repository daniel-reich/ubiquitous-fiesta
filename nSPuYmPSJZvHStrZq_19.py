
def oddeven(lst):
    a =[lst.count(x) for x in lst if x % 2 == 0]
    b = [lst.count(x) for x in lst if x % 2 != 0]
    if a < b:
        return True
    else:
        return False

