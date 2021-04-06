
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    a=list(str_A) 
    c=list(str_Z)
   
    for i in ind_Z:
        del a[i]
        a.insert(i,"-")
    new_a=[ord(i) for i in a if i != "-"]
​
    for i in ind_A:
        del c[i]
        c.insert(i,"-")
    new_c=[ord(i) for i in c if i != "-"]
    
    sum_a,sum_c = 0,0
    for i in range(len(new_a)):
        if new_a[i]-new_c[i] > 0:
            sum_a += new_a[i]-new_c[i] 
        else :
            sum_c += new_c[i] - new_a[i] 
    return { "A":sum_a , "Z": sum_c }

