
def hats(lst):
    target, lines = lst
    if target == 1:
        minutes = min(lines)
        return '{} minutes'.format(minutes) if minutes > 1 else '1 minute'
    num, den = 0, 1
    for i in range(len(lines)):
        product = 1
        for j in range(len(lines)):
            if j != i:
                product *= lines[j]
        num += product
        den *= lines[i]
    minutes = int(target * den / num)
    n_cycles = minutes // min(lines)
    minutes = n_cycles * min(lines)
    n_hats = sum(minutes // line for line in lines)
    while n_hats < target:
        minutes += 1
        n_hats = sum(minutes // line for line in lines)
    return '{} minutes'.format(minutes) if n_hats == target else None

