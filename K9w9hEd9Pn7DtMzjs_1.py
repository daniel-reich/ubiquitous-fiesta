
def high_low(txt):
  nums = [int(t) for t in txt.split(' ')]
  return '{} {}'.format(max(nums), min(nums))

