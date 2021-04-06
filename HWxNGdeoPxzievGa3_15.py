
def is_strange_pair(txt1, txt2):
    try:
        return (len(txt1)==0 and len(txt2)==0) or (txt1[0]==txt2[-1] and txt1[-1]==txt2[0])
    except: return False

