
import fractions
def simplify_frac(f):
  return str(fractions.Fraction(int(f[:f.index('/')]),int(f[f.index('/')+1:])))

