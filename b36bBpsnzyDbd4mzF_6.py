
def imposter_formula(i, p):
  if i <= 3:
    comp = 100 * (i / p)
    print(str(round(comp)) + '%')
    return str(round(comp)) + '%'

