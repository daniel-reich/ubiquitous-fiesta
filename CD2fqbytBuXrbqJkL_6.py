
def can_build(txt1, txt2):
    l1 =  [a for a in txt1.replace(' ', '')]
    l2 =  [a for a in txt2.replace(' ', '')]
    try:
        for i in l1[:]:
            if i in l2:
                l2.remove(i)
                l1.remove(i)
        return len(l1) == 0
    except:
        return False

