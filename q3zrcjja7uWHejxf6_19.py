
def negative_sum(chars):
    import re
    return sum([num for num in [int(d) for d in re.findall(r'-?\d+', chars)] if num < 0])

