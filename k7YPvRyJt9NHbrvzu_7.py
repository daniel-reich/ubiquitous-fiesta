
def football(score): 
  points = [2,3,6,7,8]
  v = [1] + [0 for k in range(score)]
​
  for i in range(5): 
    for j in range(points[i],score+1):
      v[j] += v[j-points[i]]
  return v[-1]

