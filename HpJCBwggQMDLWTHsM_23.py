
def average_word_length(txt):
  S = txt.split()
  T = sum(len([letter for letter in i if letter.isalpha()]) for i in S)
  return round(T/len(S),2)

