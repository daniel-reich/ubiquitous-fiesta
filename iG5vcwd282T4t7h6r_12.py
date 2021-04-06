
def str_to_dict(lst):
  return {item.split('=')[0]:item.split('=')[1] for item in lst}

