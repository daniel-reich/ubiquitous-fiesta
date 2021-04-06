
def josephus(n):
  def solve(circle, kill=False):
    for i in range(len(circle)):
      if circle[i] == 'a':
        if kill:
          circle = circle[:i] + 'd' + circle[i+1:]
          if circle.count('a') == 1:
            return circle
        kill = not kill
    return solve(circle, kill)
    
  return False if n <= 1 else solve('a'*n).find('a')

