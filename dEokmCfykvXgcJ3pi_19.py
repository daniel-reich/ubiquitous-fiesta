
def first_arg(*args):
  try :
    a, *b = args
    return a
  except (ValueError) : return None
  
def last_arg(*args):
  try : 
    *a, b = args
    return b
  except (ValueError) : return None

