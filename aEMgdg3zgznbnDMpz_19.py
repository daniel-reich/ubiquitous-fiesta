
def rotated_words(txt):
  sp_char = ["H", "I", "N", "O", "S", "W", "X", "Z" ]
  if txt:
    count = 0
    words = set(txt.split(" "))
    print(words)
    for word in words:
      l = 0
      for char in word:
        if char in sp_char:
          l +=1
      if l == len(word):
        count+=1
    return count
  else:
    return 0

