
def reverse_odd(txt):
  return " ".join([word[::-1] if len(word)%2!=0 else word for word in txt.split()])

