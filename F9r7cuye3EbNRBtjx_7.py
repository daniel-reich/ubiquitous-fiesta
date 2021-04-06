
def string_builder(s):
  q, num_q = [''], []
  for i,c in enumerate(s):
    if c.isdigit():
      if s[i-1].isdigit():
        num_q[-1] += c
      else:
        num_q.append(c)
    elif c == '[':
      q.append('')
    elif c == ']':
      x = q.pop()
      q[-1] += x*int(num_q.pop())
    else:
      q[-1] += c
  return q[-1]

