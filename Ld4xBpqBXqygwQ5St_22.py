
class Testpaper:
  def __init__(self, subject, markscheme, pass_mark):
    self.subject = subject
    self.markscheme = markscheme
    self.pass_mark = pass_mark
    
​
class Student:
  def __init__ (self):
    self.tests_taken = 'No tests taken'
  
  def take_test(self, exam, stu_exam):
    marks = sum([1 if exam.markscheme[i] == stu_exam[i] else 0 for i in range(len(exam.markscheme))])*100/len(exam.markscheme)
    if type(self.tests_taken) == str:
      self.tests_taken = {}
    if marks >= int(exam.pass_mark[:-1]):
      self.tests_taken[exam.subject] = 'Passed! ('+str(int(round(marks)))+'%)'
    else:
      self.tests_taken[exam.subject] = 'Failed! ('+str(int(round(marks)))+'%)'

