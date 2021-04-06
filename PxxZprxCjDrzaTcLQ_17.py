
def vowel_links(txt):
  vow = ["e", "u", "i", "o", "a"]
  words = txt.split(" ")
  print(words)
  err = 0
  for i in range(len(words) - 1):
    if (words[i][-1] in vow and words[i+1][0] in vow) == True:
      err += 1
  return(err != 0)

