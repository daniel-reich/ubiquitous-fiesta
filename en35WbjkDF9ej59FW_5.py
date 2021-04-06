
def ends_add_to_10(nums):
 count=0
 for i in range(0,len(nums)):
  num_str=str(nums[i])
  if num_str[0].isdigit():
   first=num_str[0]
  else:
   first=num_str[1]
  # print(first)
  if int(first)+int(num_str[-1]) == 10:
   count+=1
   # print(count)
 return count

