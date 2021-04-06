
def pi(n):
  pi_fract=start= 3*10**int(n*2)
  for i in range(1,int(n*10)):
    start*=2*i-1
    start//=2*i*4
    pi_fract+=start//(2*i+1)
  return '3.' + str(pi_fract)[1:n+1]

