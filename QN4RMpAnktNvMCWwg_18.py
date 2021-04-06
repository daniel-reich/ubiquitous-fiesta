
def id_mtrx(n):
   
    empty = []
    empty_2 = []
    if isinstance(n,str):
        return "Error"
    if n > 0:
        for i in range(n):
            for j in range(n):
                if i == j:
                    empty_2.append(1)
                else:
                    empty_2.append(0)
        a = [empty_2[x:x+n] for x in range(0,len(empty_2),n)]
        return a
               
    if n < 0:
        for b in range(abs(n)):
            for c in range(abs(n)):
                if b == c:
                    empty.append(1)
                else:
                    empty.append(0)
        k = [empty[l:l+abs(n)] for l in range(0,len(empty),abs(n))]
        k.reverse()
        return k
    if n == 0:
        return 0

