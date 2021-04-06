
def missing_letter(lst):
  for i in range(len(lst)-1):
    if ord(lst[i]) != ord(lst[i+1]) - 1:
      return chr(ord(lst[i]) + 1)

