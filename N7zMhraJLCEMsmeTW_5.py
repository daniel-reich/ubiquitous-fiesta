
def min_swaps(string):
  type_a=''.join('1' if i%2 else '0' for i in range(len(string)))
  type_b=''.join('0' if i%2 else '1' for i in range(len(string)))
  return min(sum(not type_a[i]==string[i] for i in range(len(string))),sum(not type_b[i]==string[i] for i in range(len(string))))

