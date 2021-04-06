
def missing_letter(lst):
  la = [ord(x) for x in lst]
  max_l = max(la)
  min_l = min(la)
​
  for i in range(min_l + 1, max_l):
    if i not in la:
      return chr(i)

