
def longest_run(lst):
  run = []
  longestRun = 0
  for num in lst:
    if len(run) == 0:
      run.append(num)
    elif (run[-1]+1 == num or run[-1]-1 == num) and len(run) == 1:
      run.append(num)
    elif len(run)>1 and ((run[-1]+1 == num and run[-2]+2 == num) or (run[-1]-1 == num and run[-2]-2 == num)):
      run.append(num)
    else:
      if longestRun < len(run):
        longestRun = len(run)
      run = [num]
      
  return max([longestRun, len(run)])

