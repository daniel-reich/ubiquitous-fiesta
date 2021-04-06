
def dice_score(throw):
    s={}
    throw.sort()
    for i in throw:
        s[i]= throw.count(i)
    sum=0
    for key,val in s.items():
      if key == 1 and val ==3:
          sum = sum+1000
      elif key ==1:
          sum = sum+val*100
      elif key ==5:
          sum = sum + val*50
      elif key in [2,3,4,5,6] and val ==3:
          sum = sum + key*100
    return sum

