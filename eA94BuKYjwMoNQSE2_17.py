
def correct_signs(s):
    numlst = []
    sign = [] 
    res = []
    count = 0 
    if '<' in s and ('>' not in s): 
        a = s.split('<')
        for num in a:
            numlst.append(int(num))
        for x in range(len(numlst)-1):
            if (numlst[x] < numlst[x+1]):
                count += 1 
        if count == len(numlst) -1: 
            return True 
        else:
            return False 
    elif '>' in s and ('<' not in s):
        a = s.split('>')
        for num in a:
            numlst.append(int(num))
        for x in range(len(numlst)-1):
            if (numlst[x] > numlst[x+1]):
                count += 1 
        if count == len(numlst) -1: 
            return True 
        else:
            return False 
    elif '>' in s and '<' in s:
        for x in s: 
            if x.isdigit()==False and x != ' ': 
                sign.append(x)
        a = s.split('>')
        for equation in a[0]:
            b = equation.split('<')
            for i in b:
                if i.isdigit(): 
                    i = int(i)
                    numlst.append(i) 
        for x in range(len(numlst)-1):
            if (numlst[x] < numlst[x+1]):
                count += 1 
        if count == len(numlst) -1: 
            partial = True 
        else:
            partial = False 
        if partial == True: 
            if (numlst[-1] > int(a[1])):
                return partial 
            else: 
                return False 
        else:
            return False

