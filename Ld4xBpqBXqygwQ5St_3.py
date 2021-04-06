
class Testpaper:
  
  def __init__(self,subject,markscheme,passmark):
    self.subject = subject
    self.markscheme = markscheme
    self.pass_mark = passmark
    
class Student:
  def __init__(self):
    self.tests_taken = 'No tests taken'
  
  def take_test(self,paper,scores):
    final_score = sum(a==b for a,b in zip(scores,paper.markscheme))
    perc = round((final_score/len(paper.markscheme))*100)
    p = 'Passed!' if perc >= int(paper.pass_mark[:-1]) else 'Failed!'
    if self.tests_taken == 'No tests taken':
      self.tests_taken = dict()
    self.tests_taken[paper.subject] = '{} ({}%)'.format(p,perc)

