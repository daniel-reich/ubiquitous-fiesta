
seq = [0, 1]
a, b = 0, 1
while True:
    a, b = b, (a + b) % 3
    seq.append(b)
    if seq[-2:] == [0, 1]:
        break
        
def normal_sequence(n):
    return seq[n % 8 - 1]

