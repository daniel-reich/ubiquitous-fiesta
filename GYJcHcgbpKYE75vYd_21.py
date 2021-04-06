
def return_end_of_number(num):
  teen = ['11', '12', '13']
  ords = {1: 'ST', 2: 'ND', 3: 'RD'}
  rem = num % 10
  numeral = str(num)
  end = '-'
  if numeral[-2:] in teen:
    end += 'TH'
  elif rem in ords:
    end += ords[rem]
  else:
    end += 'TH'
  return '{}{}'.format(numeral, end)

