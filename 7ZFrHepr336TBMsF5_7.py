
def percentage_changed(old, new):
  per = (int(new[1:])/int(old[1:])*100)-100
  change = 'decrease' if per<0 else 'increase'
  return '{}% {}'.format(round(abs(per)),change)

