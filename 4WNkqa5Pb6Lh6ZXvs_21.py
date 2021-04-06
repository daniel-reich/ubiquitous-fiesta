
import re
def evaluate_polynomial(poly, num):
  if poly:
    if not re.search(r'[^x\()\d\/\^\+\-\*]', poly) and '//' not in poly:
      poly=re.sub(r'(\d)(\()', r'\1*\2', poly)
      poly=re.sub(r'(x)(\()', r'\1*\2', poly)
      poly=re.sub(r'(\d)(x)', r'\1*\2', poly)
      poly=poly.replace('^', '**').replace('x', str(num))
      return eval(poly)
    else:
      return "invalid"
  return 'invalid'

