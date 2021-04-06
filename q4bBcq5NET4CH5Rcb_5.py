
valueDict = {
  "half": 0.5,
  "quarter": 0.25,
  "eighth": 1/8,
  "sixteenth": 1/16
}
  
def jay_and_bob(txt):
  result = 0
  for value in valueDict:
    if txt == value:
      result = 28*valueDict[value]
      if (result).is_integer():
        result = int(result)
  result = str(result)
  return(result + " grams")

