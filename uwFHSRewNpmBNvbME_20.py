
def same_vowel_group(w):
  vowelpresent = []
  vowels = ["a","e","i","o","u"]
  res = []
  for i in w[0]:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
      if i not in vowelpresent: vowelpresent.append(i)
      if i in vowels: vowels.remove(i)
  for i in w:
    flag=0
    for j in vowelpresent:
      if j not in i:
        flag=1
        break
    for k in i:
      if k in vowels:
        flag=1
        break
    if flag==0: res.append(i)
  return res

