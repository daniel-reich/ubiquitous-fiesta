
def special_reverse(s, c):
  stringArr = s.split()
​
  for word in stringArr:
    if word[0] == c:
      stringArr[stringArr.index(word)] = "".join(reversed(word))
    
  return " ".join(stringArr)

