
def is_super_d(n):
    for d in range(2, 10):
        x = d * (n**d)
        if d *str(d) in str(x):
            return 'Super-' + str(d) + ' Number'
    return 'Normal Number'

