
def is_there_consecutive(lst, n, times):
  if str(n)*times == "":
    return not n in lst
  else : return str(n)*times in "".join(map(str,lst))

