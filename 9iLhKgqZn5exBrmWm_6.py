
def ascending(st):
    for sub_len in range(1,len(st)//2+1):
        if len(st) % sub_len != 0: continue
        num_of_sub_nums = len(st) // sub_len
        nums = [int(st[i*sub_len:(i+1)*sub_len]) for i in range(num_of_sub_nums)]
        min_ = min(nums)
        if list(map(lambda x:x-min_,nums)) == list(range(num_of_sub_nums)): return True
    return False

