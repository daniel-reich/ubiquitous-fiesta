
def special_reverse(s, c):
  word_list = s.split(" ")
  rev_list = []
  for word in word_list:
    if word[0] == c:
      word = word[::-1]
    rev_list.append(word)
  print(word_list)
  return " ".join(rev_list)

