
def build_staircase(height, block):
  ans=[]
  step=1
  for i in range(height):
    temp=[]
    temp+=[block]*step
    temp+=['_']*(height-step)
    ans.append(temp)
    step+=1
  for i in ans:
    print(i)
  return ans

