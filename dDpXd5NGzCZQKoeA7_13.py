
def num_args(func):
  i = 0
  while True:
    try: func(*i*[i]); return i
    except: i+=1

