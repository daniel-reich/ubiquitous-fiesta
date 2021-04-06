
def missing_letter(lst):
  for a, b in zip(lst, lst[1:]):
    if ord(a) + 1 != ord(b):
      return chr(ord(a) + 1)

