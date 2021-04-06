
def break_point(num):
 output=False
 num_str=str(num)
 # go through string
 for i in range(0,len(num_str)):
  sum_left=0
  sum_right=0
  # create sums left and right of index
  for l in range(0,i):
   sum_left+=int(num_str[l])
  #print(sum_left)
  for r in range(i,len(num_str)):
   sum_right+=int(num_str[r])
  #print(sum_right)
  if sum_left == sum_right:
   output=True
   break
 return output

