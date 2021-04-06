
def ruth_aaron(n):
  sn_, sn, sn1 = prime_facts(n-1), prime_facts(n), prime_facts(n+1)
  kinds = 0
​
  if sum(set(sn)) == sum(set(sn1)):
    which = "Ruth"
    kinds+=1
  if sum(set(sn_)) == sum(set(sn)):
    which = "Aaron"
    kinds+=1
  if sum(sn) == sum(sn1):
    which = "Ruth"
    kinds+=2
  if sum(sn_) == sum(sn):
    which = "Aaron"
    kinds+=2
  return [which,kinds] if kinds else False
​
​
def prime_facts(n):
  facts, i = [], 2
  while n>1:
    while n%i == 0:
      facts+= [i]
      n=n//i
    i+= 1
  return facts

