
def hidden_anagram(text, phrase):
  
  class Word:
    
    def find_anagrams(word):
      from itertools import permutations as p
      
      perms = list(p(word, len(word)))
      return [''.join(perm) for perm in perms]
    
    def __init__(self, word):
      self.word = word.lower().replace(' ', '')
  #   self.anagrams = Word.find_anagrams(self.word)
      self.l8r_counts = {}
      for l8r in set(self.word):
        count = self.word.count(l8r)
        self.l8r_counts[l8r] = count
    
    def __len__(self):
      return len(self.word)
    
    def is_anagram(self, phrase):
      for l8r in set(phrase):
        if l8r not in self.l8r_counts.keys():
          return False
        else:
          count = phrase.count(l8r)
          if count != self.l8r_counts[l8r]:
            return False
      return True
  
  
  class Sentence:
    
    def __init__(self, sentence):
      self.sentence = sentence.lower().replace(' ', '')
      valid = 'abcdefghijklmnopqrstuvwxyz'
      
      for item in self.sentence:
        if item not in valid:
          self.sentence = self.sentence.replace(item, '')
          
    def find_anagram(self, word):
      anagram_length = len(word)
      
      poss_anagrams = []
      
      for n in range(len(self.sentence)):
        try:
          s = self.sentence[n:n+anagram_length]
        except IndexError:
          s = self.sentence[n:]
        
        if len(s) < anagram_length:
          break
        else:
          poss_anagrams.append(s)
      
      for anagram in poss_anagrams:
        if word.is_anagram(anagram) == True:
          return anagram
      
      return 'noutfond'
      
  phrase = Word(phrase)
  sentence = Sentence(text)
  
  return sentence.find_anagram(phrase)

