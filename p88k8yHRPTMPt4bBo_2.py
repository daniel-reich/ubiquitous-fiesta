
def countVowels(string):
   vowels = ['a','e','i','o','u']
   total = 0
   for s in string:
      if s in vowels:
         total += 1
   return total

