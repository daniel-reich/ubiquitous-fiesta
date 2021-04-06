
def who_passed(students):
  lst = [i for i in students if all([grade(x) for x in students[i]])]
  return sorted(lst)
​
def grade(s):
  return len(set(s.split('/')))==1

