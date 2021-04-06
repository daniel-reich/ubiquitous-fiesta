
def face_interval(num):
    if type(num) != list:
        return ":/"
    face = max(num) - min(num)
    return ":)" if face in num else ":("

