
def longest_run(lst):
  longest = 1
  for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
      if abs(lst[j] - lst[i]) == len(lst[i: j + 1]) - 1:
        sublength = len(lst[i: j + 1])
        if sublength > longest:
          longest = sublength
  return longest

