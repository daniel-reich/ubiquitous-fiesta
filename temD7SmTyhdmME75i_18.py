
def to_boolean_list(word):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  bit_lst = [True if alphabet.index(x) % 2== 0 else False for x in word]
  return [bool(bit) for bit in bit_lst]

