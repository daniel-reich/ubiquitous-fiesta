
def get_best_student(grades):
  ans = []
  aa = []
​
  for k, v in grades.items():
    a = sum(v)
    ans.append(a)
    aa.append(k)
    
  ans1 = ans.index(max(ans))
  
  return aa[ans1]
​
​
print(get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
}))

