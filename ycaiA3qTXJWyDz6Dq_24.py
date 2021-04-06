
def consonants(word):
  counter1 = 0
  vowels = ['a','e','i','o','u']
  not_vowels = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
  for i in word.lower():
    if i in not_vowels:
      counter1 += 1
  return counter1
​
​
​
def vowels(word):
 vowles = ['a','e','i','o','u']
 counter = 0 
 for i in word.lower():
  print(i)
  if i in vowles:
    counter = counter + 1
 return counter
​
print(vowels('Jameel SAEB'))
print(consonants('He|\o mY Fr*end'))

