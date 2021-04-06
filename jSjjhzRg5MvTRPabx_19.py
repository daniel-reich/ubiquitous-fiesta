
def sentence(nouns):
    nouns = [
    "an " + noun if noun[0] in "aeiou" else "a " + noun 
    for noun in nouns
  ]
    nouns[-1] = "and " + nouns[-1] + "."
    nouns[0] = nouns[0][1:]
    return "A" + ", ".join(nouns[:-1]) + " " + nouns[-1]

