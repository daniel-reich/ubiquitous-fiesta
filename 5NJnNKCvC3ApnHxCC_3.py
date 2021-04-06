
def mubashir_function(a, b):
  ref = lambda x: sum(map(int, str(x)))
  return ref(a) * ref(b)

