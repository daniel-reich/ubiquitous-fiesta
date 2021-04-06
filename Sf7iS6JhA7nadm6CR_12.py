
def divisibility_rule(n):
    seq = [1, 10, 9, 12, 3, 4]
    newlist = [n]
    newlist2 = []
    index = 0
    rev_number = '1'
    while True:
        total = 0
        rev_number = str(newlist[0])[::-1]
        for i in range(len(rev_number)):
            if index == len(seq):
                index = 0
            total += int(rev_number[i]) * seq[index]
            index += 1
        newlist2.append(total)
        if newlist2.count(total) > 1:
            return total
        newlist[0] = total
        rev_number = str(total)[::-1]
        total = 0
        index = 0
    print(rev_number)

