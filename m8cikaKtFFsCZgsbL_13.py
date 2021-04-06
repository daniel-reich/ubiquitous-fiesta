
import math
​
def waterjug(start, goal):
  global found
  hst = {}
  stc = []
  found = False
  def asStr(ls):
    return str(ls[0]) + ',' + str(ls[1]) + ',' + str(ls[2])
​
  def pour(state, _from, _to, _other):
    res = [-1,-1,-1]
    cap = start[_to] - state[_to]
    amt = min(cap, state[_from])
    if amt is 0:
      return
    res[_from] = state[_from] - amt
    res[_to] = state[_to] + amt
    res[_other] = state[_other]
    stc.append(res)
  
  def iter(state):
    global found
    try:
      h = hst[asStr(state)]
      return
    except:
      hst[asStr(state)] = True
      #print(asStr(state))
      #print(asStr(goal))
      if asStr(state) == asStr(goal):
        found = True
        return
      pour(state, 0, 1, 2)
      pour(state, 0, 2, 1)
      pour(state, 1, 0, 2)
      pour(state, 1, 2, 0)
      pour(state, 2, 0, 1)
      pour(state, 2, 1, 0)
    
  count = 0
  run = True
  left = []
  stc.append([0, 0, start[2]])
  while run:
    run = False
    left = stc
    stc = []
    for x in left:
      run = True
      iter(x)
    if found:
      return count
    count += 1
  return 'No solution.'

