
def return_end_of_number(num):
  x = {'1': "-ST", '2': "-ND", '3': "-RD"}
  if len(str(num)) > 1 and str(num)[-2] == '1':
    return str(num) + '-TH'
  return str(num) + x[str(num)[-1]] if (str(num)[-1] in '123') else str(num) + "-TH"

