
def ecg_seq_index(n):
    result = [1, 2]
    num = 1
    fac = [x for x in range(2, result[-1] + 1) if result[-1] % x == 0]
    while result[-1] != n:
        num += 1
        
        if num not in result:
            fac_num = [x for x in range(2, num + 1) if num % x == 0]
            if list(set(fac).intersection(fac_num)):
                result.append(num)
                fac = fac_num
                num = 1
    return len(result) - 1

