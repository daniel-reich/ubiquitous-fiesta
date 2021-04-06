
def int_to_vlq(n):
  result = [n % 128]; n //= 128
  while n > 0:
    result.insert(0, n % 128 + 128)
    n //= 128
  return result
​
def vlq_to_int(lst):
  return sum((byte % 128) * 128 ** (len(lst) - i) for i, byte in enumerate(lst, 1))

