
def average_word_length(txt):
  words = txt.split(' ')
  ans = [len(i.strip(",.?!''")) for i in words]
  return round(sum(ans) / len(words), 2)

