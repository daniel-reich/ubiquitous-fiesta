
def lambda_to_def(code: str) -> str:
  name = code[:code.find('=')].rstrip()
  code = code[code.find('lambda') + 6:].lstrip()
  quotes = []
  for i in range(len(code)):
    if code[i] == ':' and len(quotes) == 0:
      break
    elif code[i] in ("'", '"'):
      if len(quotes) > 0 and code[i] == quotes[-1]:
        quotes.pop()
      else:
        quotes.append(code[i])
  args, func = code[:i].rstrip(), code[i + 1:].strip()
  return 'def {}({}):\n\treturn {}'.format(name, args, func)

