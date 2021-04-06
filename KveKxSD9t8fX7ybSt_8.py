
def final_countdown(ls):
    num_seq, seq = 0, []
    for i, x in enumerate(ls):
        print(i,x)
        if x == 1:
            sub_seq = []
            sub_ls = ls[:i + 1]
            sub_ls.reverse()
            for j, y in enumerate(sub_ls):
                print(j, y, j + 1)
                if y == sub_ls[j-1] + 1 or j == 0:
                    sub_seq.append(y)
                else:
                    break
            sub_seq.reverse()
            seq.append(sub_seq)
            num_seq += 1
    return [num_seq, seq]

