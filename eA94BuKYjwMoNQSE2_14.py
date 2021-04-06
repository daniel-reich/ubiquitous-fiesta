
def correct_signs(txt):
​
  tmp = txt.split()
  nums = tmp[0::2]
  syms = tmp[1::2]
  
  for i in range(len(nums) - 1):
    if (int(nums[i]) < int(nums[i+1]) and syms[i] == "<") or (int(nums[i]) > int(nums[i+1]) and syms[i] == ">"):
      return True
    else:
      return False

