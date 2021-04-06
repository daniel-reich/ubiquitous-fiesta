
def jay_and_bob(txt):
  conversion=28
  switch={"half":conversion/2,
  "third":conversion/3,
  "quarter":conversion/4,
  "fifth":conversion/5,
  "seventh":conversion/7,
  "sixth":conversion/6,
  "eighth":conversion/8,
  "sixteenth": conversion/16}
  if switch.get(txt)%1 == 0:
    return  str((int)(switch.get(txt)))+" grams"
  return  str(switch.get(txt))+" grams"

