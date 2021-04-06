
def holey_sort(lst):
  dic = {"4":1, "6":1, "9":1, "0":1, "8":2}
  result = [sum(dic.get(n,0) for n in num) for num in map(str,lst)]
  return sorted(lst, key=lambda x: result[lst.index(x)])

