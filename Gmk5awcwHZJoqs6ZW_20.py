
def largest_island(lst):
    if len(lst)==1:
        return 1
    else:
        rows,cols = len(lst),len(lst[0])
        dict1 = {}
        ind = 0
        con = 0
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j] != 0:
                    p= [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                    num_del = []
                    for k in range(len(p)):
                        if p[k][0]<0 or p[k][1]<0 or p[k][0]>rows-1 or p[k][1]>cols-1:
                            num_del.append(k)
                    for m in range(len(num_del)):
                        p.remove(p[num_del[m]])
                        num_del[m:] = [x-1 for x in num_del[m:]]
                    
                    
                    for n in p:
                        if n not in dict1.values() and lst[n[0]][n[1]] != 0:
                            dict1[ind] = n
                            ind +=1
                            
        for v in dict1.values():
            for w in dict1.values():
                if 0<((w[0]-v[0])**2+abs(w[1]-v[1])**2)**0.5<2:
                    con +=1
                    break        
        if con:                        
            return con
        return 1

