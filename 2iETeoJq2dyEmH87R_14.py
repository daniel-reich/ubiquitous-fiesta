
def count_digits(n, d):
  squares = [i*i for i in range(n+1)]
  
  return sum(1 for i in squares for j in str(i) if str(j) == str(d))

