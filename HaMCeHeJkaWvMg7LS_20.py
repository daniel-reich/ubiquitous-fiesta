
def sun_loungers(beach):
  count = 0
  beach = list(beach)
  for i in range(len(beach)):
    if beach[i]=='0':
      left = beach[max(i-1,0)]
      right = beach[min(i+1,len(beach)-1)]
      if left==right=='0':
        count+=1
        beach[i] = '1'
  return count

