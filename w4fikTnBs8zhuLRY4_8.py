
rep_set = lambda n: [] if not n else rep_set(n-1) + [rep_set(n-1)]

