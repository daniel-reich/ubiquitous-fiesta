
def findShortestWords(txt):
  txt_formatted = ''.join([x.lower() for x in txt if x.isalpha() or x == ' ']).split()
  word_lengths = [len(y) for y in txt_formatted]
  return sorted([z for z in txt_formatted if len(z) == min(word_lengths)])

