
import math
def c_cipher(msg, keyword):
    enc_flag = False
    for i in range(len(msg)):
        if not msg[i].isalnum():
            enc_flag = True
            break
            
    new_msg = [msg[i].lower() for i in range(len(msg)) if msg[i].isalnum()]
    
    #natural sequence
    key_seq = [keyword[i] for i in range(len(keyword))]
    key_dict = {key_seq[i]:i for i in range(len(key_seq))}
    key_dic_dec = {key_dict[i]:i for i in key_dict}
    
    
    key_seq_sort = sorted(key_seq)
    key_dict_sort = {key_seq_sort[i]:i for i in range(len(key_seq_sort))}
    
    msg_len = len(new_msg)
    key_len = len(key_seq)
    row = math.ceil(msg_len/key_len)
    col = key_len
    
    #enc
    if enc_flag:
        msg_dict = {}
        for i in range(col):
            temp_str = ""
            for j in range(row):
                if j*col + i < msg_len:
                    temp_str += new_msg[j*col + i]
                else:
                    temp_str += 'x'
            msg_dict[i] = temp_str
​
        result = ""
        key_seq.sort()
        for ele in key_seq:
            current = key_dict[ele]
            result += msg_dict[current]
    else:
        orginal_cols = [] 
        for ele in key_seq:
            current = key_dict_sort[ele] #original row
            orginal_cols.append(msg[current*row:(current+1)*row])
        
        result = ""
        for i in range(row):
            for j in range(col):
                result += orginal_cols[j][i] 
    
    
    return result

