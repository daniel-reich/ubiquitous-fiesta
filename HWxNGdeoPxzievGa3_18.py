
def is_strange_pair(txt1, txt2):
    if txt1 == '' and txt2 == '':
        return True
    elif (txt1 == '' and txt2 != '') or (txt2 == '' and txt1 != ''):
        return False
    elif txt1[-1] == txt2[0] and txt1[0] == txt2[-1]:
        return True
    else:
        return False

