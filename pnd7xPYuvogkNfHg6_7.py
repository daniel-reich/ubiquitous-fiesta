
def get_best_student(d):
    o={}
    for key,item in d.items():
        o[key]=sum(item)/len(item)
    return max(o, key=o.get)

