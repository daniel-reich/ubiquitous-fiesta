
def wurst_is_better(txt):
  saus = ["kielbasa", "chorizo", "moronga", "salami", "sausage", "andouille", "naem", "merguez", "gurka", "snorkers", "pepperoni"]
  arr = txt.split(" ")
  for i in range(len(arr)):
    if arr[i].lower() in saus:
      arr[i] = "Wurst"
  return ' '.join(arr)

