
def word_search(text,lst):
    text_lst = [i.lower() for i in text]
    text_array = []
    for i in range(8):
        temp = []
        for j in range(8): 
            temp.append(text_lst[i*8 + j])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    
    for i in range(8):
        temp = []
        for j in range(8): 
            temp.append(text_lst[i + j*8])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    temp = []
    
    for i in range(8):
        for j in range(i,8):
            temp.append(text_lst[j*8+j-i])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    
        
    for i in range(8):
        for j in range(i):
            temp.append(text_lst[j*8+(7-i+j)])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
​
    for i in range(8):
        for j in range(i):
            temp.append(text_lst[j*8+i-j])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    
        
    for i in range(8):
        for j in range(i,8):
            temp.append(text_lst[j*8+(7+i-j)])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    
​
    for e in lst:
        found = False
        for e2 in text_array:
            if e2.find(e) != -1:
                found = True
                break
        if not found:
            return False
    
    
    return True

