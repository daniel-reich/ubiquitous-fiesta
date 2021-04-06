
class Testpaper:                      # Multiple choice tests
  def __init__(self, subject, marks, pass_mark):
    self.subject    = subject
    self.markscheme = marks
    self.pass_mark  = pass_mark
​
class Student:
  def __init__(self):
    self.tests_taken = "No tests taken"
​
  def take_test(self, results, answers):
    subject, marks, pass_mark = results.subject, results.markscheme, results.pass_mark
    percentage = round((len([marks[i] for i, x in enumerate(marks) if marks[i]==answers[i]]) / len(marks)) * 100)
    final = "Failed!" if percentage < int(pass_mark[:-1]) else "Passed!"
    if self.tests_taken == "No tests taken": self.tests_taken = {}
    self.tests_taken.update({subject : final + " (" + str(percentage) + "%)"})

