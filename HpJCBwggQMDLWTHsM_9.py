
def average_word_length(txt):
  txt, tot = txt.split(), sum(sum(1 for c in w if c.isalpha()) for w in txt)
  return round(tot / len(txt), 2)

