
def sorting_steps(lst):
    
    a = (lst)
    b= sorted(a)
    s = []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]> a[j]:
                a[j], a[i] = a[i], a[j]
                s.append((i,j))
                
                if a == b:
                    return s                      
    return s

