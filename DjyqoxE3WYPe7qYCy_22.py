
def reverse_odd(txt):
  return " ".join(
    word if len(word) % 2 == 0 else word[::-1]
    for word in txt.split(" ")
  )

