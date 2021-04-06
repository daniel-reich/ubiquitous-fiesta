
def balanced(lst):
 half1=lst[0:int(len(lst)/2)]
 sum1=0
 for i in range(0,len(half1)):
  sum1+=half1[i]
 half2=lst[int(len(lst)/2):len(lst)]
 sum2=0
 for k in range(0,len(half2)):
  sum2+=half2[k]
 # print('half1',half1)
 # print('sum1',sum1)
 # print('half2',half2)
 # print('sum2',sum2)
 output=[]
 if sum1 > sum2:
  output.extend(half1)
  output.extend(half1)
 elif sum1 < sum2:
  output.extend(half2)
  output.extend(half2)
 else:
  output.extend(lst)
 return output

