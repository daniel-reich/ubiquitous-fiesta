
flipping_bits = lambda n:int(''.join(str(int(i)^1) for i in bin(n)[2:].zfill(32)),2)

