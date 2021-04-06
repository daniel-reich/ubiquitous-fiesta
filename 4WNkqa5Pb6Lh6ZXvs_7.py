
import re
​
def evaluate_polynomial(poly, num):
  if re.search('^$|//|[^^\dx/+()-]', poly): 
    return 'invalid'
  poly = poly.replace('^', '**')
  poly = re.sub('(?<=\d|\))(?=x|\()|(?<=x|\))(?=\d|\()', '*', poly)
  return eval(poly.replace('x', str(num)))

