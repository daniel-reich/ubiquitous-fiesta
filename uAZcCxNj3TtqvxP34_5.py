
def mode(nums):
 # create set --> unique elements
 nums_set=set(nums)
 #print(nums_set)
 count_dict={}
 # go through unique elements
 for element in nums_set:
  # count occurences
  count=0
  for i in range(0,len(nums)):
   if nums[i] == element:
    count+=1
  # update dictionary
  count_dict.update({element:count})
 #print(count_dict)
 # determine highest counts
 highest=1
 for c in count_dict.values():
  if c > highest:
   highest=c
 #print(highest)
 # create list with nums that have the highest count
 output=[]
 for keys in count_dict.keys():
  if count_dict[keys] == highest:
   output.append(keys)
 return sorted(output)

