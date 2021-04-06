
who_passed = lambda x: sorted(n for n 
  in x.keys() if all(eval(s) == 1 for s in x[n]))

