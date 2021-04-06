
def missing_letter(lst):
  for i in range(0, len(lst) - 1):
    if lst[i + 1] != chr(ord(lst[i]) + 1):
      return chr(ord(lst[i]) + 1)

