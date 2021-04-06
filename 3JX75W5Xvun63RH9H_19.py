
def describe_num(n):
  arr = ["brilliant", "exciting", "fantastic", "virtuous", "heart-warming", "tear-jerking", "beautiful", "exhilarating", "emotional", "inspiring"]
  brr = []
  for i in range(1, 11):
    if n % i == 0:
      brr.append(arr[i-1])
  
  return "The most " + " ".join(brr) + " number is {}!".format(n)

