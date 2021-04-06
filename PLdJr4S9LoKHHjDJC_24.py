
def identify(*cube):
  lgth, lgth_cbe = [len(i) for i in cube], len(cube)
  mx = max(lgth)
  miss = [mx - l for l in lgth]
  return 'Full' if sum(miss) == 0 and lgth_cbe == mx else 'Non-Full' if lgth_cbe != mx and sum(miss) == 0 else 'Missing {}'.format(sum(miss))

