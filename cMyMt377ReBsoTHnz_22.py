
def dict_to_list(d):
  return sorted([(k, v) for k, v in d.items()], key=lambda x: x[0])

