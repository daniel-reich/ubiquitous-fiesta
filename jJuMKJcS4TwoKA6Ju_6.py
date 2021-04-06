
def dial(txt):
    ph = {'abc':2,'def':3,'ghi':4,"jkl":5,"mno":6,"pqrs":7,'tuv':8,"wxyz":9}
    s = ''
    for char in txt:
        if str(char).isalpha():
            for k in ph.keys():
                if char.lower() in k :
                    s+=str(ph[k])
                    break
        else:s+=char
    return s

