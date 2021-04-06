
def digital_cipher(message, key):
    msg_lst = []
    for i in range(len(message)): # making the list of order
        chr = message[i]
        msg_lst.append(ord(chr) - 96) # a == 96
​
    key_lst = []
    key = str(key)
    for e in key:
        e = int(e)
        key_lst.append(e)
    while len(key_lst) < len(msg_lst):
        key_lst = key_lst * 2
    key_lst = key_lst[0: len(msg_lst)]
​
    end_lst = []
    for t in range(len(msg_lst)):
        end_lst.append(msg_lst[t] + key_lst[t])
    return end_lst

