
abc = {
  'a': '1',
  'e': '2',
  'i': '3',
  'o': '4',
  'u': '5'
}
​
def replace_vowel(word):
  return ''.join( [ abc[l] if l in 'aeiou' else l for l in word ] )

