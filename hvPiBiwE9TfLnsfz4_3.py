
def generate_word(n, initial=True, seq=[]):
    if initial and n < 2:
        return "invalid"
    if initial:
        if n == 2:
            return "b, a"
        seq = ["b", "a"]
        return generate_word(n - 2, False, seq[:])
    if n == 0:
        return ", ".join(seq)
    seq.append(seq[-2] + seq[-1])
    return generate_word(n - 1, False, seq[:])

