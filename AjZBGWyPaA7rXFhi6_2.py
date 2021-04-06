
def min_swaps(s1, s2):
  return bin(int(s1, 2) ^ int(s2, 2)).count('1') // 2

