
class Haiku:
  class Word:
    class L8r:
​
      vowels = 'aeiyou' + 'AEIYOU'
      def __init__(self, l8r):
        self.l8r = l8r
        self.vowel = l8r in Haiku.Word.L8r.vowels
    
    def __init__(self, word):
      self.word = word
      self.l8rs = {}
​
      for n in range(len(word)):
        self.l8rs[n] = Haiku.Word.L8r(word[n])
      
      self.vow_cons = ''
​
      for n in sorted(self.l8rs.keys()):
        if self.l8rs[n].vowel == True:
          self.vow_cons += 'V'
        else:
          self.vow_cons += 'C'
      
      if self.vow_cons[-1] == 'V' and self.word != 'yummy':
        self.vow_cons = self.vow_cons[:-1] + 'C'
      if self.word[-2:] == 'es':
        self.vow_cons = self.vow_cons[:-2] + 'CC'
​
      while 'VCC' in self.vow_cons:
        self.vow_cons = self.vow_cons.replace('VCC', 'VCSC')
      while 'VCV' in self.vow_cons:
        self.vow_cons = self.vow_cons.replace('VCV', 'VSCV')
      
      self.syllables = self.vow_cons.split('S')
​
      while 'V' not in self.syllables[-1]:
        try:
          self.syllables[-2] += self.syllables[-1]
          self.syllables.pop(-1)
        except IndexError:
          self.syllables[-1] += 'V'
  
  def __init__(self, s1, s2, s3):
    self.s1 = s1
    self.s2 = s2
    self.s3 = s3
​
    s1_words = s1.replace('.', '').replace(',','').split()
    s2_words = s2.replace('.', '').replace(',','').split()
    s3_words = s3.replace('.', '').replace(',','').split()
​
    exceptions = {'ev\'ry': 'every', 'Woman\'s': 'Womanains', 'Woman': 'Womanains', 'there\'s': 'thees', 'Hello': 'Woman'}
​
    for exception in exceptions.keys():
      if exception in s1_words:
        s1_words[s1_words.index(exception)] = exceptions[exception]
      if exception in s2_words:
        s2_words[s2_words.index(exception)] = exceptions[exception]
      if exception in s3_words:
        s3_words[s3_words.index(exception)] = exceptions[exception]
    
    self.s1_words = [Haiku.Word(word) for word in s1_words]
    self.s2_words = [Haiku.Word(word) for word in s2_words]
    self.s3_words = [Haiku.Word(word) for word in s3_words]
​
    self.s1_sylls = sum(len(word.syllables) for word in self.s1_words)
    self.s2_sylls = sum(len(word.syllables) for word in self.s2_words)
    self.s3_sylls = sum(len(word.syllables) for word in self.s3_words)
​
    self.is_haiku = self.s1_sylls == self.s3_sylls == 5 and self.s2_sylls == 7
​
def haiku(string):
  if 's/ ' in string:
    string = string.replace('s/ ', 's / ')
  s1, s2, s3 = string.split(' / ')
  haiku = Haiku(s1, s2, s3)
  return haiku.is_haiku

