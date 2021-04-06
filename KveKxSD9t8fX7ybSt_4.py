
def final_countdown(lst):
    ones = [i for i in range(len(lst)) if lst[i] == 1]
    cds = []
    for one in ones:
        cd = []
        i = 0
        while lst[one-i] == 1+i:
            i += 1
            cd = [i] + cd
        cds.append(cd)
    return [len(ones), cds]

