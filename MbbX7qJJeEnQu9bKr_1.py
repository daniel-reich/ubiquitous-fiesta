
def max_occur(text):
  arr = [0 for i in range(127)]
  maxCount = -1
  ans = -1
  for i in text:
    arr[ord(i)] += 1
  for i in range(127):
    if (arr[i] > maxCount):
      maxCount = arr[i]
      ans = i
  if arr[ans] == 1:
    return "No Repetition"
  return [chr(i) for i in range(127) if arr[i] == maxCount]

