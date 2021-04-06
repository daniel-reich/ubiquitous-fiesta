
def sun_loungers(beach):
  counter = 0
  i = 0
​
  while i < len(beach):
    if (beach[i] == "1"):
      i += 2
    elif (beach[max(0, i - 1)] == "1"):
      i += 1
    elif (beach[min(len(beach) - 1, i + 1)] == "1"):
      i += 3
    else:
      counter += 1
​
      i += 2
      
  return counter

