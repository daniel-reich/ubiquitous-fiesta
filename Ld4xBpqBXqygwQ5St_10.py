
class Testpaper:
​
  def __init__ (self, subject, markscheme, pass_mark):
    self.subject = subject
    self.markscheme = markscheme
    self.pass_mark = pass_mark
​
class Student:
​
  def __init__ (self):
    self.tests_taken = "No tests taken"
    
  def take_test(self, paper, marks):
    Qs = len(marks)
    As = marks
    RAs = paper.markscheme
    sc = int(round(100*sum(1 for i in range(Qs) if As[i] == RAs[i])/Qs,0))
    if self.tests_taken == "No tests taken":
      self.tests_taken = {}
    self.tests_taken[paper.subject] = ("Failed!" if sc < int(paper.pass_mark[:-1]) else "Passed!") + " (" + str(sc) + "%"+ ")"

