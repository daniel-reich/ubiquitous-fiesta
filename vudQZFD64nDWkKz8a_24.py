
def grant_the_hint(txt):
​
  class Secret:
​
    def __init__(self, txt):
      self.t = txt
​
      words = txt.split()
​
      hidden = []
​
      for word in words:
        hide = ''
        for l8r in word:
          hide += '_'
        hidden.append(hide)
      
      self.view = ' '.join(hidden)
      self.index = 0
​
    def hint(self):
​
      if self.t == self.view:
        return True
      
      words = self.view.split()
      act_words = self.t.split()
​
      new_words = []
​
      for n in range(len(words)):
        hid_word = words[n]
        act_word = act_words[n]
​
        new_words.append(act_word[:self.index+1] + hid_word[self.index+1:])
        
      self.index += 1
      self.view = ' '.join(new_words)
      return self.view
​
  message = Secret(txt)
​
  tr = [message.view]
  c = 0
​
  while tr[-1] != True and c < 1000:
    tr.append(message.hint())
    c+=1 
  
  return tr[:-1]

