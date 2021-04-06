
def face_interval(num):
    if num == str(num):
        return(':/')
    num.sort(reverse=False)
    if (num[len(num)-1] - num[0]) in num:
        return':)'
    else:
        return':('

