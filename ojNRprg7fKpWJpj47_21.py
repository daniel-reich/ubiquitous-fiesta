
def shift_sentence(txt):
  lst = [i for i in txt.split()]
  lst2 = [i[0] for i in lst]
  return " ".join(lst2[i-1][0] + lst[i][1:] for i in range(len(lst)))

