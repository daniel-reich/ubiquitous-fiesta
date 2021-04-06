
def final_countdown(lst):
    cnt, seq = 0, []
    for i in range(len(lst)):
        if lst[i] != 1:
            continue
        cur = [1]
        j = i - 1
        while j >= 0 and lst[j] == lst[j+1] + 1:
            cur.append(lst[j])
            j -= 1
        seq.append(cur[::-1])
        cnt += 1
    return [cnt, seq]

