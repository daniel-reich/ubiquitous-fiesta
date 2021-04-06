
def rail_fence_cipher(msg, rails):
    rail_lst = build_rail_sequence(msg, rails)           
    return rail_encrypt(msg, rail_lst)
​
def rail_encrypt(msg, rail_lst):
    cipher = {}
    cipher_txt = ""
    for i in range(max(rail_lst) + 1):
        cipher[i] = ""
    for i in range(len(msg)):
        cipher[rail_lst[i]] += msg[i]
    for v in cipher.values():
        cipher_txt += v
    return cipher_txt
​
def build_rail_sequence(msg, rails):
    char_cnt = 0
    order = []
    down = False
    indx = 0
    while char_cnt < len(msg):
        order.append(indx)
        if indx == rails-1:
            down = True
        elif indx == 0:
            down = False
       
        if down:
            indx -= 1
        else:
            indx += 1
        char_cnt += 1
    return order

