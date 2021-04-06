
def harmonic(n):
  #numbers = {0:0, 1:1}
  #result = numbers[n] if n in numbers else (1.0 / n) + harmonic(n-1)
  #return round(result,3)
  return 0 if n == 0 else round(sum(1.0/d for d in range(1,n+1)),3)

