
def reverse_complement(input_sequence):
    l=len(input_sequence)
    s=""
    for i in range(0,l):
        b=input_sequence[i]
        if b == "A":
            c="U"
        elif b == "U":
            c="A"
        elif b == "G":
            c="C"
        elif b == "C":
            c="G"
        s=c+s
    return s

