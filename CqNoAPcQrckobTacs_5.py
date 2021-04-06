
def missing_letter(lst):
  for i in range(len(lst)):
    if chr(ord(lst[i]) + 1) != lst[ i + 1]:
      return chr(ord(lst[i]) + 1)

