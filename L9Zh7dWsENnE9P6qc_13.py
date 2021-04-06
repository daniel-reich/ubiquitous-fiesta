
def josephus(people):
    l = people - (1 << (people.bit_length() - 1))
    score = 2*l + 1
    return score

