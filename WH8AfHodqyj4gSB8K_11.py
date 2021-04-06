
def is_authentic_skewer(s):
  letters = [i for i in s if i.isalpha()]
  skewers = ''.join([' ' if i.isalpha() else i for i in s]).split()
  if len(set(skewers))!=1:
    return False
  return len(letters)>=1 and len(skewers)+1==len(letters) and all([letters[i] in 'AEIOU' if i%2==1 else letters[i] not in 'AEIOU' for i in range(len(letters))])

