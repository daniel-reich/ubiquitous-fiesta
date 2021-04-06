
import scipy.integrate
def integral(b, m, n):
  f=lambda x:(b+1)*(x**b)
  return round(scipy.integrate.quad(f,m,n)[0])

