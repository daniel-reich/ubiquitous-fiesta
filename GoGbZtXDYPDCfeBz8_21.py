
def magic(txt):
​
  nums = [ num for num in txt.split(' ') ]
  magic = int(nums[0]) * int(nums[1])
​
  return str(magic) == nums[-1][-1 * len(str(magic)):]

