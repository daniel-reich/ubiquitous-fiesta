
import re
lambda_format = re.compile(r'(.*?)\s+=\s+lambda\s+(.*?):(.*)')
​
def lambda_to_def(code):
  m = lambda_format.match(code)
  if not m:
    return None
  name, args, expr = m.group(1), m.group(2), m.group(3)
  
  colon_replaced = False
  def fix_quote(quote):
    nonlocal args, expr, colon_replaced
    if args.count(quote) % 2 != 0:
      if not colon_replaced:
        args += ':'
        colon_replaced = True
      rouge_quote = expr.find(quote)
      args += expr[:rouge_quote + 1]
      expr = expr[rouge_quote + 1:]
      
  fix_quote("'")
  fix_quote('"')
  if expr[0] == ':':
    expr = expr[1:]
  return "def {}({}):\n\treturn {}".format(name.strip(), args.strip(), expr.strip())

