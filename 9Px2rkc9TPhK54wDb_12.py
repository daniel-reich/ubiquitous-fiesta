
def ecg_seq_index(num):
    seq = [1, 2]
    possible = []
    number = 2
    while seq[-1] != num:
        number = number + 1
        possible.append(number)
        for a in possible:
            works = 1
            for b in range(2, a+1):
                if a % b == 0 and seq[-1] % b == 0:
                    seq.append(a)
                    works = 2
                    break
            if works != 1:
                possible.remove(a)
                break
    result = seq.index(num)
    return result;

