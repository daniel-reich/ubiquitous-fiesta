
def longest_time(h, m, s):
  time = {h : h,
          m : (m // 60),
          s : (s // 3600)
          }
​
  return [k for k,v in time.items() if max(time.values()) == v][0]

