
def turn_calc(n):
    s = str(n).replace('.', '')[::-1]
    return s.translate(str.maketrans('123456780', 'IZEHSGLBO'))

