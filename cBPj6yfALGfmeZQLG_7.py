
def vertical_txt(txt):
  lst = txt.split(" ")[::-1]
  m = max(len(string) for string in lst)
  lst_copy = [string+" "*(m-len(string)) for string in lst]
  return [[string[i] for string in lst_copy][::-1] for i in range(m)]

