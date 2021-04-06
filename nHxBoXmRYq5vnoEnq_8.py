
def vowels(string):
  nem = []
  for i in string:
      nem.append(i)
  #print(nem)
  vowel = ["a","i","e","o","u"]
  total = 0
  for j in nem:
      if j in vowel:
          total = total + 1
  return total
      
print(vowels("apple"))

