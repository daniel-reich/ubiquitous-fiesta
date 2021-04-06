
def partition(txt, n):
  lst = []
  string = ""
  for i in range(0, len(txt), n):
    string += txt[i:i+n]
    lst.append(string)
    string = ""
  return lst
print(partition("c++", 2))

