
def turn_calc(num):
  return ''.join('OIZEHSGLB-'[int(i)] for i in str(num).replace('.', '')[::-1])

