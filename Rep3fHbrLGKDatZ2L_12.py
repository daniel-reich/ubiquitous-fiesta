
def complete_pattern(s):
  print(s)
  for i in range(1,len(s)):
      missing=set()
      for a,b in zip(s[:i]*(len(s)//i+1),s):
        if a!=b:
          if b=="_":
            missing.add(a)
          elif a=="_":
            missing.add(b)
          else:
            missing.add('_')
​
      if len(missing)==1: return missing.pop()

