
def intersection(h1, h2):
    d1 = {}
    d2 = {}
    final_list = []
    
    for i in h1.keys():
    
        if i in h2.keys():
            d1[i] = h1[i]
​
    final_list.append(d1)
​
    for j in h2.keys():
        if j in h1.keys():
            d2[j] = h2[j]
​
    final_list.append(d2)
    
    return final_list

