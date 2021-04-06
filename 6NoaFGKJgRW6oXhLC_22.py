
def sum_of_vowels(sentence):
  lst = list(sentence)
  for i in range(len(lst)):
    a = lst.count("a") + lst.count("A")
    e = lst.count("e") + lst.count("E")
    i = lst.count("i") + lst.count("I")
    
  return a*4 + e*3 + i

