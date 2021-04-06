
def dance(lst,parameter):
    ladies = []
    gents = []
    for couple in lst:
        ladies.append(couple[0])
        gents.append(couple[1])
    if parameter == 'women':
        ladies = ladies[::-1]
    else:
        gents = gents[::-1]
    return [[ladies[i], gents[i]] for i in range(len(lst))]

