
def sum_of_vowels(sentence):
  a,e,i = (sentence.count("a")+sentence.count("A")),(sentence.count("e")+sentence.count("E")),sentence.count("i")+sentence.count("I")
  return (a*4) + (e*3) + i

