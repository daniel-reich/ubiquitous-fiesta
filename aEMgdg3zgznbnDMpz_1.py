
def rotated_words(txt):
  chars = 'HINOSXZWM'
  return sum(all(j in chars for j in i) for i in set(txt.split()))

