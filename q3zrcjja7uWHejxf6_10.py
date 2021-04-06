
def negative_sum(chars):
    nums = [int(_) for _ in  ''.join([c  if c in "+-0123456789" else ' ' for c in chars]).replace('-', ' -').split()]
    return sum([n for n in nums if n < 0])

