
def missing_letter(lst):
  return [chr(ord(x) - 1) for i, x in enumerate(lst) if ord(lst[i]) - ord(lst[i - 1]) > 1][0]

