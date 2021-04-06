
def is_super_d(n):
  c = [i for i in range(2, 10) if str(i) * i in str(i * n ** i)]
  return "Super-{} Number".format(c[0]) if len(c) > 0 else "Normal Number"

