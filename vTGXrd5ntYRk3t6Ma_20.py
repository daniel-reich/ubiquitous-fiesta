
"""
An isogram is a word that has no repeating letters, consecutive or nonconsecutive. 
Create a function that takes a string and returns either True or False depending 
on whether or not it's an "isogram".
"""
​
def is_isogram(txt):
  to_lower = txt.lower()
  
  for letter in to_lower:
    if to_lower.count(letter) > 1:
      return False
  return True

