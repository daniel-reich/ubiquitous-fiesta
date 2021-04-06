
def digital_cipher(message, key):
    num_lst = []
    key_str = str(key)
    key_lst = []
    key_mask = []
    az_dict = {}
    az_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # create a key list
    for k in key_str:
        key_lst.append(int(k))
        # create dict to map letters to numbers
        num = 1
    for i in range(len(az_lst)):
        az_dict[az_lst[i]] = num
        num += 1
    # get list of int's from message
    for i in message:
        num_lst.append(az_dict[i])
    # create a key of the proper length
    key_length = len(key_lst)
    m_length = len(num_lst)
    key_mod = m_length % key_length
    key_int = int((m_length - key_mod) / key_length)
    key_leftover = []
    for i in range(key_mod):
        key_leftover.append(key_lst[i])
    for i in range(key_int):
        key_mask = key_mask + key_lst
    key_mask = key_mask + key_leftover
    # add the key_mask to the num_lst and return it
    cipher = []
    val = 0
    count = 0
    for i in num_lst:
        val = num_lst[count] + key_mask[count]
        cipher.append(val)
        count += 1
    return cipher

