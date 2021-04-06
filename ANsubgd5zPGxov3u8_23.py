
def initialize(names):
  return [' '.join(n[0]+'.' for n in name.split()) for name in names]

