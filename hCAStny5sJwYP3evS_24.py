
def is_early_bird(_range, n):
    return_value = []
    seq = ""
    length = len(list(str(n)))
​
    # creating seq!
    for i in range(0, _range + 1):
        seq = seq + str(i)
​
    # Number of repetition of n in seq
    for k in range(0, len(seq) - length + 1):
        if seq[k:k + length] == str(n):
            a = []
            for r in range(k, k + length):
                a.append(r)
            return_value.append(a)
​
    seq2 = ""
    for i in range(0, n + 1):
        seq2 = seq2 + str(i)
    ideal = len(seq2) - length
​
    for j in range(0, len(return_value)):
        if return_value[j][0] < ideal:
            return_value.append("Early Bird!")
            break
​
    return return_value

