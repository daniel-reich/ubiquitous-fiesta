
def n_tables_plus_one(num):
    Final = ''
    for item in range(1,10+1):
        Final += str((num*item)+1)+','
    return Final[:-1]

