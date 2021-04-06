
def wurst_is_better(txt):
  sausages = ["kielbasa","chorizo","moronga","salami","sausage","andouille","naem","merguez","gurka","snorkers","pepperoni"]
  result = []
  for word in txt.split():
    if word.lower() in sausages:
      result.append("Wurst")
    else:
      result.append(word)
  return " ".join(result)

