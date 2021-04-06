
def normal_sequence(n):
  dict = { 1: 0, 2: 1, 3: 1, 4: 2, 5: 0, 6: 2, 7: 2, 0: 1}
  return dict[n % 8]

