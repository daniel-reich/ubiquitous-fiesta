
def complete_bracelet(bracelet):
    '''
    Returns True if bracelet has at least 2 consecutive identical subsequences
    of length at least 2 as per the instructions.
    '''
    size = len(bracelet)
    max_seq  = size // 2  # longest subsequence which could repeat
    seg_size = 2  # size of subsequence being checked for repetition
    ptr = 0  # index to start check from
​
    while seg_size <= max_seq:
        okay = True
        while ptr + seg_size * 2 <= size:
            if bracelet[ptr:ptr+seg_size] != bracelet[ptr+seg_size:ptr+2*seg_size]:
                okay = False
                break # try next biggest size
            ptr += seg_size
            
        if okay and size % seg_size == 0:
            return True   # got to end of bracelet with all repeating
        
        seg_size += 1
        ptr = 0  # try again with bigger subsequence size
​
    return False

