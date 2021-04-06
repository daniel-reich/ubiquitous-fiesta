
def shadow_sentence(a, b):
  if len(a) != len(b): return False
  lst1 = a.split()
  lst2 = b.split()
  res = 0
  for i in range(len(lst1)):
    word = lst1[i]
    for j in range(len(word)):
      if not word[j] in lst2[i]:
        res += 1
  return res == len(''.join(lst1))

