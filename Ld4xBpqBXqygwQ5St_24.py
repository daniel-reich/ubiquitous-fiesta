
class Testpaper:
  def __init__(self, sub, sch, ps):
    self.subject = sub
    self.markscheme = sch
    self.pass_mark = ps
​
class Student:
  def __init__(self):
    self.tests_taken = 'No tests taken'
  
  def take_test(self, ppr, tst):
    
    if type(self.tests_taken) is str:
      self.tests_taken = {}
      
    suc = 0
      
    for x in range (len(tst)):
      if tst[x] == ppr.markscheme[x]:
        suc+=1
        
    rate = round(suc/len(tst)*100)
    
    if rate >= int(ppr.pass_mark.strip('%')):
      self.tests_taken[ppr.subject] = 'Passed! ({}%)'.format(rate)
    else:
      self.tests_taken[ppr.subject] = 'Failed! ({}%)'.format(rate)

