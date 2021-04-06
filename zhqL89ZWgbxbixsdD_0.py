
is_exact = lambda n, k=1, i=1: is_exact(n, k*i, i+1) \
  if k < n else ([n, i-1] if k == n else 'Not exact!')

