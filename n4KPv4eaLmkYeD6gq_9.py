
def face_interval(num):
    if isinstance(num, list) == False:
        return ':/'
    if max(num) - min(num) in num:
        return ':)'
    else:
        return ":("

