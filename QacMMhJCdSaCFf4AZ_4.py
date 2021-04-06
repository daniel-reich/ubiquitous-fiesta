
def sequence_generator(seq):
    a_a, c_a = seq[1] - seq[0], 2 * seq[0] - seq[1]
    a_g, c_g = seq[1] / seq[0], seq[0] * seq[0] / seq[1]
​
    def seq_a(n):
        return a_a * n + c_a
​
    def seq_g(n):
        return round(pow(a_g, n) * c_g)
​
    if seq_a(3) == seq[2] and seq_a(4) == seq[3] and seq_a(5) == seq[4]:
        return seq_a
    elif seq_g(3) == seq[2] and seq_g(4) == seq[3] and seq_g(5) == seq[4]:
        return seq_g

