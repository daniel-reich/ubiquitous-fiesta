
def is_super_d(n):
    for i in range(2, 10):
        num = str(i * n**i)
        if str(i)*i in num:
            return 'Super-{} Number'.format(i)
    return 'Normal Number'

