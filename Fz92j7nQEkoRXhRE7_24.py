
def jumping_frog(n,l):
  tree=[[]]
  for i in range(len(l)):
    if i+l[i]>=len(l):
      tree[0]+=[i]
      if i==0:
        return 2
  for steps in range(1,len(l)):
    tree+=[[]]
    for x in tree[steps-1]:
      for i in range(len(l)):
        if i+l[i]==x or i-l[i]==x:
          tree[steps]+=[i]
          if i==0:
            return steps+2
  return 'no chance :-('

