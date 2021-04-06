
x = lambda n: [[int(any([i==j, i==n-j-1])) 
    for i in range(n)] for j in range(n)]
diamond = lambda n: [x(n)[n//2:-1] + x(n)[:n//2+n%2], 
          'perfect cut' if n%2==1 else 'good cut']

