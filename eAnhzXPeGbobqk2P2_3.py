
def century(year):
    century = (year // 100) + 1 if (year % 100 != 0) else (year // 100)
    suffix = 'th' if century <= 20 else 'st'
    return '{}{} century'.format(century, suffix)

