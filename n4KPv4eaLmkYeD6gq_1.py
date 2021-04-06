
def face_interval(num):
    if type(num) == list:
        x = max(num) - min(num)
        if x in num:
            return ":)"
        else:
            return ":("
    else:
        return ":/"

