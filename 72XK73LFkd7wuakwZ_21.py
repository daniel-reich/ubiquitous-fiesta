
def junction_or_self(n):
  return [m for m in range(n) if m + sum(int(d) for d in str(m)) == n][::-1] or "Self"

