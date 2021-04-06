
def secret(txt):
​
  words = txt.split(".")
  result = "<"+words[0]+" class='"
  for i in range(1, len(words)):
    result += words[i]+" "
  result = result.rstrip()
  result += "'></"+words[0]+">"
  return result

