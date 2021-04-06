
def n_tables_plus_one(num):
    b = num + 1
    a = [str(b)]
    for i in range(9):
        b += num
        a.append(str(b))
    return ','.join(a)

