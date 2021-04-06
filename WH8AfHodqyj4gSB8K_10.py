
def is_authentic_skewer(s):
    vowels = list('AEIOU')
    if s[0] == '-':
        return False
  
    #  check if spacing is consistent
    letters = [x for x in s if x.isalpha()]
    d = (s.index(letters[1]) - 1) * '-'
    if not d:
        return False
    if s.split(d) != letters:
        return False
    
    if letters[0] in vowels and letters[-1] in vowels:
        return False
​
    if set(letters[1::2]).difference(vowels):
        return False
    
    if any(x in vowels for x in letters[::2]):
        return False
    
    return True

