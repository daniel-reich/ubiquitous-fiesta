
def complete_bracelet(lst):
    string = ''.join(list(map(str, lst)))
    patterns = [''.join(list(map(str, lst))[:x]) for x in range(1, int(len(lst)/2+1))]
    for i in range(1,int(len(lst)/2)):
        if patterns[i]*int(len(lst)/len(patterns[i])) == string:
            return True
        else: 
            continue
    return False

