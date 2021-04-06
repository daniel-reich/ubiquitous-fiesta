
class Testpaper:
  def __init__(t,s,m,p): t.subject,t.markscheme,t.pass_mark=s,m,p
class Student:
  def __init__(s): s.tests_taken="No tests taken"
  def take_test(s,t,a):
    if type(s.tests_taken)!=dict: s.tests_taken={}
    p = round(sum(a[1]==b[1] for a,b in zip(a,t.markscheme))*100/len(a))
    s.tests_taken.update({t.subject:"%sed! (%s%%)"%
      (["Pass","Fail"][p<int(t.pass_mark[:2])],p)})

