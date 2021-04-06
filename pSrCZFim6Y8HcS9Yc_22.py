
def convert(deg):
  convert={'*C': lambda x:round(1.8*x+32), '*F': lambda x:round((x-32)/1.8)}
  try:
    return str(convert[deg[-2:]](int(deg[:-2])))+'*'+chr(137-ord(deg[-1:]))
  except: return "Error"

