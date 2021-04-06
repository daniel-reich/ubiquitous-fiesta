
def count_digits(n, d):
  st=''.join([y for y in [str(x**2) for x in range(n+1)] if str(d) in y])
  return st.count(str(d))

