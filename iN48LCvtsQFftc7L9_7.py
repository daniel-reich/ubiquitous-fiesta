
def word_search(letters, words):
  words = [w.upper() for w in words]
  s1 = [letters[i:i+8] for i in range(0,len(letters),8)]
  s2 = [''.join(i) for i in map(list,zip(*s1))]
  s3 = [[] for _ in range(15)]
  s4 = [[] for _ in range(15)]
​
  for i in range(8):
    for j in range(8):
      s3[i+j].append(s1[j][i])
      s4[i-j-7].append(s1[j][i])
  s3 = [''.join(i) for i in s3]
  s4 = [''.join(i) for i in s4]
  test = s1+s2+s3+s4
​
  for w in words:
    check = 0
    for t in test:
      if w in t or w[::-1] in t:
        check = 1
        break
  
    if check == 0:
      return False
  return True

