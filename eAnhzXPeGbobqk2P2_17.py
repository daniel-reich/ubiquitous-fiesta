
def century(year):
 a=[]
 for e in range(0,3000,100):
    a.append(e)
 for i in range(len(a)):
    if a[i]>2000:
        return str(int(str(year)[:2])+1)+'st'+' century'
        break
    elif a[i]==year:
        return str(int(str(year)[:2]))+'th'+' century'
        break
    elif a[i]>year:
        return str(int(str(year)[:2])+1)+'th'+' century'
        break

