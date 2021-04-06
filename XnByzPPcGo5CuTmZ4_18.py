
def kix_code(addr):
    addr_lst = addr.split(',')
    post_code = addr_lst[2][:8].replace(' ', '')
    digit_idx = 0
    for idx, c in enumerate(addr_lst[1]):
        if c.isnumeric():
            digit_idx = idx
            break
    house_num = (addr_lst[1][digit_idx:].replace(' ', 'X')
                 .replace('-', 'X').replace('/', 'X').upper())
    return post_code + house_num

