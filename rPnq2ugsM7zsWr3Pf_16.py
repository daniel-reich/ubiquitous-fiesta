
def find_all_digits(nums):
  numbers = set("0123456789")
  for num in nums:
    for n in str(num): 
      if n in numbers:
        numbers.remove(n)
    
    if numbers == set():
      return num
  
  else:
    return "Missing digits!"

