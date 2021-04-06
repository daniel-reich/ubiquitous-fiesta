
def average_word_length(txt):
  import re
  lst = list(map(len, re.sub(r'\W+', ' ', txt).split()))
  return round(sum(lst)/len(lst),2)

