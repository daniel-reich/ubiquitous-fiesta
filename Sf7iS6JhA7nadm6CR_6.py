
def divisibility_rule(n):
    seq = [1, 10, 9, 12, 3, 4]
    rvrsed_n = str(n)[::-1]
    rvrsed_n_lst = list(rvrsed_n)
    output = 0
    for i in range(len(rvrsed_n_lst)):
        if i < len(seq):
            output += int(rvrsed_n_lst[i]) * seq[i] 
        else:
            j = i
            while j >= len(seq):
                j = j-6
            output += int(rvrsed_n_lst[i]) * seq[j] 
​
    if n != output:
        return divisibility_rule(output)
    elif n == output:
        return n

