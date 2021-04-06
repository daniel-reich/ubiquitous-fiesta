
def encrypt(msg, keyword):
    msg = msg.lower().replace(' ', '').replace('.', '')
    splt_msg = [msg[i : i + len(keyword)] for i in range(0, len(msg), len(keyword))]
    
    # add x's to end of message if needed
    if len(splt_msg[-1]) != len(keyword):
        for _ in range(len(keyword) - len(splt_msg[-1])):
            splt_msg[-1] += 'x'
    
    # create ordered number list from letters in keyword
    ord_num_lst = ['x' for _ in range(len(keyword))]
    buf_txt = [i for i in keyword]
    for idx, let in [j for j in enumerate(sorted([i for i in keyword]))]:
        nidx = buf_txt.index(let)
        ord_num_lst[nidx] = idx
        buf_txt[nidx] = None  # remove letter to account for reoccuring letters
​
    # combinding columns and forming new string
    encrypted_msg = ''
    count = 0
    for i in ord_num_lst:
        idx = ord_num_lst.index(count)
        for j in splt_msg:
            encrypted_msg += j[idx]
        count += 1
    return encrypted_msg
​
​
def decrypt(msg, keyword):
    # start by getting alphabetically ordered values from keyword
    ord_num_lst = ['x' for _ in range(len(keyword))]
    buf_txt = [i for i in keyword]
    for idx, let in [j for j in enumerate(sorted([i for i in keyword]))]:
        nidx = buf_txt.index(let)
        ord_num_lst[nidx] = idx
        buf_txt[nidx] = None  # remove letter to account for reoccuring letters
​
    # number of rows needed
    num_rows = int(len(msg) / len(keyword))
    
    # go through each row and recreate original message
    org_msg = ''
    place_hldr = []
    for pos in ord_num_lst:
        place_hldr.append(msg[:num_rows])
        msg = msg[num_rows:]
    count = 0
    for _ in range(len(place_hldr[0])):
        for col in ord_num_lst:
            org_msg += place_hldr[col][count]
        count += 1
    return org_msg
​
​
def c_cipher(msg, keyword):
    return encrypt(msg, keyword) if len(msg.split()) != 1 else decrypt(msg, keyword)

