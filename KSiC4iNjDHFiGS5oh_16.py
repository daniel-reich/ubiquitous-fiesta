
def is_super_d(n) :
    for i in range(2, 10) :
        total_value = i * n**i
        super_digit = str(i) * i
        if str(super_digit) in str(total_value) :
            return 'Super-%s Number' % (i)
        elif i == 9:
            return 'Normal Number'

