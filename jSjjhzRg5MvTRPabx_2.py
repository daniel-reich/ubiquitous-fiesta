
def sentence(words):
  final = []
  for i in words:
    final.append("a"+("n"*(i[0] in "aeiou"))+" "+i)
  sentence = ""
  for i in range(len(final)-1):
    sentence += final[i]+", "
  sentence = sentence[:-2]+" and "+final[-1]+"."
  return sentence.capitalize()

