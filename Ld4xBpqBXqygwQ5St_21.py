
class Testpaper:
  
  def __init__(self, subject, markscheme, pass_mark):
    self.subject = subject
    self.markscheme = markscheme
    self.pass_mark = pass_mark
    
class Student:
  
  def __init__(self, tests_taken='No tests taken'):
    self.tests_taken = tests_taken
    
  def take_test(self, test, answers):
    
    mark = []
    for i in test.markscheme:
      mark.append([a for a in i])
      
    ans = []
    for i in answers:
      ans.append([a for a in i])
    
    score=0
    for a in ans:
      for m in mark:
        if a[0] == m[0]:
          if a[1]==m[1]: score += 1
    
    tot = int(round(score / len(test.markscheme) * 100,0))
    per = str(tot) + '%)'
    if tot >= int(test.pass_mark[0:-1]):
      out = 'Passed! (' + per
    else:
      out = 'Failed! (' + per
    
    if self.tests_taken == 'No tests taken':
      self.tests_taken = {test.subject:out}
    else:
      self.tests_taken[test.subject] = out

