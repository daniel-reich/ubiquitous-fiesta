
def fibo_word(n):
  coma = ", "
  lst = ["b","a"]
  out = "b"
  a = ""
  if(n < 2):
    return("invalid")
  else:
    for i in range(n - 2):
      lst.append(lst[-1] + lst[-2])
    for i in range(len(lst)-1):
      out = out + coma + lst[i + 1]
    return(out)

