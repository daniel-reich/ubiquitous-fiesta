
def char_at_pos(r, s):
  res = [r[-i] for i in range(1 if s == 'odd' else 2, len(r)+1, 2)][::-1]
  return "".join(res) if isinstance(r, str) else res

