
class Testpaper:
  
  def __init__(self, subject, markscheme, pass_mark):
    self.subject = subject
    self.markscheme = markscheme
    self.pass_mark = pass_mark
  
​
class Student:
  
  def __init__(self, tests_taken="No tests taken"):
    self.tests_taken = tests_taken
    
  def take_test(self, paper, answers):
    if not isinstance(self.tests_taken, dict):
        self.tests_taken = {}
    
    score = 0
    for i in range(len(answers)):
      if answers[i] == paper.markscheme[i]:
        score += 1
    score = score / len(answers) * 100
​
    if score >= int(paper.pass_mark[:-1]):
      grade = "Passed!"
    else:
      grade = "Failed!"
    
    self.tests_taken[paper.subject] = "{} ({:.0f}%)".format(grade, score)

