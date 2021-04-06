
def calculate_arrowhead(lst):
  lst = "".join(lst)
  lefts = lst.count("<")
  rights = lst.count(">")
  
  maks = max(lefts, rights)
  mins = min(lefts, rights)
  
  if maks==lst.count("<"):
    return (maks-mins)*"<"
  else:
    return (maks-mins)*">"

