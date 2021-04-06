
def str_to_dict(lst):
  return {i.split('=')[0] : i.split('=')[1] for i in lst}

