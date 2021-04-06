
"""
wins get 3 points
draws get 1 point
losses get 0 points
"""
wins=3;draws=1;losses=0
​
def football_points(w,d,l):
  global wins,draws,losses
  return w*wins+d*draws+l*losses

