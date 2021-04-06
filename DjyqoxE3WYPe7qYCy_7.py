
def reverse_odd(string):
  words = string.split(" ");
  return " ".join(word[::-1] if len(word) %2 != 0 else word for word in words);

