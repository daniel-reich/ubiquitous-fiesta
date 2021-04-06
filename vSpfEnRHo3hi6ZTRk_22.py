
def free_throws(success, rows):
    s = (int(success[:-1])/100) ** rows
    s = round(s * 100)
    return str(s)+'%'

