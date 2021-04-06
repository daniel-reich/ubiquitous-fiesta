
s_pals = [0,10,20,30,40,50,1,11,21,31,41,51,2,12,22,32]
m_pals = [0,11,22,33,44,55]
h_pals = [0,1,2,3,4,5,10,11,12,13,14,15,20,21,22,23]
pals = [[h,m,s] for m in m_pals for s,h in zip(s_pals,h_pals)]
​
def palindrome_time(lst):
  s1,m1,h1,s2,m2,h2 = lst
  
  return sum(1 for p in pals if p<=[s2,m2,h2])-\
          sum(1 for p in pals if p<[s1,m1,h1])

