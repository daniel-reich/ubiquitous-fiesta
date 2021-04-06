
flipping_bits=lambda n:int(''.join(('0','1')[x=='0']for x in bin(n)[2:].zfill(32)),2)

