
def wurst_is_better(txt):
  words=txt.split()
  result=[]
  sausages = ["kielbasa","chorizo","moronga","salami","sausage","andouille","naem","merguez","gurka","snorkers","pepperoni"]
  sausages = set(sausages)
  for word in words:
    if(word.lower() in sausages):
      result.append("Wurst")
    else:
      result.append(word)
  return(" ".join(result))

