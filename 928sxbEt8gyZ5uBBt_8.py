
def wurst_is_better(txt):
  lst = txt.split(" ")
  saulst = ["kielbasa", "chorizo", "moronga", "salami", "sausage", "andouille", "naem", "merguez", "gurka", "snorkers", "pepperoni"]
  for i, x in enumerate(lst):
    if(saulst.count(x.lower())==1):
      lst[i] = "Wurst"
  return ' '.join(lst)

