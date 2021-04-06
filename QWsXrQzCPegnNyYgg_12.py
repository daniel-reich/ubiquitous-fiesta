
import scipy.integrate as integrate
def integral(b, m, n):
  return round(integrate.quad(lambda x: (b + 1) * (x ** b), m, n)[0])

