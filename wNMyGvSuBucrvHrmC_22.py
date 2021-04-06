
number_of_repeats = lambda s: max([1]+[s.count(s[:i]) for i in range(2, len(s)//2+1)
                                  if not len(s) % i])

