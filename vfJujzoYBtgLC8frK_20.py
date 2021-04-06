
def word_to_decimal(word):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  base_ = alpha.index(max(word.lower())) + 11
  lst0 = [alpha.index(txt) + 10 for txt in word.lower()]
  lst1 = lst0[:-2]
  lst2 = [lst1[(len(lst1) - 1) - i] * (base_**(i + 2)) for i in range(len(lst1) - 1, -1, -1)]
  return sum(lst2) + (lst0[len(lst0) - 2] * base_ + lst0[-1])

