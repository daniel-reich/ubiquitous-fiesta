
def palindromic_date(date):
  a= date[0:2]
  b= date[3:5]
  c=date[6:]
  s = a+b+c
  s1 = b+a+c
  return s == s[::-1] and s1 == s[::-1]
​
​
​
print(palindromic_date("02/02/2020"))

