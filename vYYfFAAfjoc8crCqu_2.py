
tree = lambda h: [' ' * (((h*2-1)-x)//2) + '#' * x +
  ' ' * (((h*2-1)-x)//2) for x in [k*2-1 for k in range(1, h+1)]]

