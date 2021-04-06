
def is_correct_aliases(names, aliases):
    caps1 = [x[0] for x in names] 
    caps2 = []
    for y in aliases:
        a = y.split(' ')
        for i in a:
            caps2 += i[0]
    index = 0
    for x in caps1:
        if x != caps2[index] or x != caps2[index+1]:
            return False
        index += 2
    return True

