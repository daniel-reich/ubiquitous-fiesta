
def which_is_larger(f, g):
  return ['f', 'g', 'neither'][[f()>g(), g()>f(), True].index(True)]

