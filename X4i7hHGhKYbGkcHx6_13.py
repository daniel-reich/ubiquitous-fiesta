
def average_index(s):
  return round(sum(ord(i) - 96 for i in s) / len(s), 2)

