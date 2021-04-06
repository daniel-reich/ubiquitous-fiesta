
def edabit_in_string(txt):
  it = iter(txt)
  return "YES" if all(any(c == ch for c in it) for ch in 'edabit') else "NO"

