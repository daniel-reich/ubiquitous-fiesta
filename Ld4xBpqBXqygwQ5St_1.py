
class Testpaper:
  def __init__(self, subject, markscheme, pass_mark):
    self.subject = subject
    self.markscheme = markscheme
    self.pass_mark = pass_mark
    
​
class Student:
  def __init__(self):
    self.tests_taken = 'No tests taken'
    
  def take_test(self, paper, answers):
    pmark = int(paper.pass_mark[:-1])
    correct = sum(a == b for a, b in zip(paper.markscheme, answers))
    perc = '{:.0%}'.format(correct / len(answers))
    msg = '{}! ({})'.format('Passed' if int(perc[:-1]) > pmark else 'Failed', perc)
    
    if type(self.tests_taken) == str:
      self.tests_taken = {paper.subject : msg}
    else:
      self.tests_taken[paper.subject] = msg

