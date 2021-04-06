
import re
def special_reverse_string(txt):
  form = re.sub(r'[^\s]', '{}', txt)
  cases = [i.isupper() for i in txt if i != " "]
  chars = [i for i in txt if i != " "]
  print(txt, form, cases, chars)
  chars = [b.upper() if a else b.lower() for a, b in zip(cases, chars[::-1])]
  return form.format(*chars)

