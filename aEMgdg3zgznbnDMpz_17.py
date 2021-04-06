
def rotated_words(txt):
  can_rotate = 'HINOSXZWM'
  return sum(all(ch in can_rotate for ch in word) for word in set(txt.split()))

