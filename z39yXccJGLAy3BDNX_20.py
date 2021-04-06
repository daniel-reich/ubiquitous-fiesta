
flipping_bits=lambda n:int(''.join(str(int(not int(x)))for x in bin(n)[2:].zfill(32)),2)

