
import math
def c_cipher(msg, keyword):
        if ' ' in msg:
            return c_cipher1(msg, keyword)
        else:
            return c_cipher2(msg, keyword)
def c_cipher1(msg, keyword): 
    cipher = ""
    key=keyword
    msg=msg.replace('.','').replace(' ','').lower() 
    k_indx = 0  
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key))   
    col = len(key)      
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('x' * fill_null)  
    matrix = [msg_lst[i: i + col]for i in range(0, len(msg_lst), col)]
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return cipher 
def c_cipher2(msg1,keyword): 
    msg = "" 
    key=keyword
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(msg1)) 
    msg_lst = list(msg1) 
    col = len(key) 
    row = int(math.ceil(msg_len / col))  
    key_lst = sorted(list(key)) 
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx])   
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
    try: 
        msg = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.")   
    return msg

