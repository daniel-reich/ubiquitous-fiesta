
class Testpaper:
  def __init__(self, subject, mark_scheme, pass_mark):
    self.subject = subject
    self.markscheme = mark_scheme
    self.pass_mark = pass_mark
  
  def get_pass_mark_as_float(self):
    return int(self.pass_mark.strip('%')) / 100
​
class Student:
  def __init__(self):
    self.__tests_taken = {}
  
  @property
  def tests_taken(self):
    return self.__tests_taken if self.__tests_taken else "No tests taken"
  
  def take_test(self, test_paper, answers):
    score = sum(1 for i, j in zip(answers, test_paper.markscheme) if i == j)
    result = score / len(test_paper.markscheme)
    passed = result >= test_paper.get_pass_mark_as_float()
    self.__tests_taken[test_paper.subject] = \
      "{}! ({:.0%})".format("Passed" if passed else "Failed", result)

