
def to_two_complement(n):
    b = bin(abs(n))[2:]
    if n >= 0:
        return b
    b = b.zfill(8)
    c = ""
    for bit in b:
        c += '1' if bit == '0' else '0'
    return bin(int("0b" + c, 2) + 1)[2:]
    
def eight_bit(exp):
    a, op, b = exp.split()
    if not (-128 <= int(a) <= 127 and -128 <= int(b) <= 127):
        return 'Overflow'
    ba = to_two_complement(int(a))
    bb = to_two_complement(int(b))
    if op == '+':
        # addition
        c = int(a) + int(b)
        if c > 127:
            return 'Overflow'
        bc = to_two_complement(int(c))
        return (c, ba + " + " + bb + " = " + bc)
    # subtraction
    c = int(a) - int(b)
    if c < -128:
        return 'Overflow'
    bc = to_two_complement(int(c))
    return (c, ba + " - " + bb + " = " + bc)

