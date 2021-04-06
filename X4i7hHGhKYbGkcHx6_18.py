
def average_index(letters):
  res = [ord(ch) - 96 for ch in letters]
  return round(sum(res) / len(res), 2)

