
def stem_plot(lst):
  stems = sorted({n//10 for n in lst})
  stlea = [[s,sorted(n%10 for n in lst if s == n//10)] for s in stems]
  return [str(p[0]) + " | " + " ".join(str(l) for l in p[1]) for p in stlea]

