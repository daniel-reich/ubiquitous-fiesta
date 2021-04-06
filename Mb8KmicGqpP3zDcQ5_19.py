
def josephus(num, step):
    if step == 1:
        return num
    ls = [i for i in range(num)]
    counter = 0
    while ls.count('-') < num - 1:
        for i in range(len(ls)):
            if ls[i] != '-' and counter != step - 1:
                counter += 1
            elif ls[i] != '-' and counter == step - 1:
                ls[i] = '-'
                counter = 0
    return list(i for i, v in enumerate(ls) if v != '-')[0] + 1

