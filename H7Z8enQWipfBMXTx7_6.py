
def fib_str(turns, sequence):
    if turns == 2:
        return ', '.join(sequence)
    else:
        sequence.append(sequence[-1]+sequence[-2])
        return fib_str(turns-1, sequence)

