
def who_passed(d):
    pas=[]
    for key, value in d.items():
        if all([eval(x)==1.0 for x in d[key]]):
            pas.append(key)
    return sorted(pas)

