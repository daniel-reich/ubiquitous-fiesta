
def is_super_d(n):
    for i in range(2, 10):
        if str(i) * i in str(i * (n ** i)):
            return 'Super-{} Number'.format(i)
    return 'Normal Number'

