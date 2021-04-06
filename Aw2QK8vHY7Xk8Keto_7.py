
def longest_word(s):
  txt = s.split()
  counter = 0
  word = ''
  for i in txt:
    if len(i) > counter:
      counter = len(i)
      word = i
  print(word)
  print(counter)
  return str(word)

