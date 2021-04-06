
lst, st = [1, 2], set([1, 2])  
def ulam(n): 
​
    i = lst[-1] +1
    while len(lst) < n:
        count = 0  
        for k in range(0, len(lst)): 
            if (i - lst[k]) in lst:
                if lst[k] != (i - lst[k]):  
                    count += 1
​
            if count >= 3:  
                break
​
        if count == 2: 
            lst.append(i)  
            st.add(i)
        i += 1
    return lst[-1]

