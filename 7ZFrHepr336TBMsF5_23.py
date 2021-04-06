
def percentage_changed(old, new):
  woohoo = 0
​
  old1 = int(old[1:])
  neww = int(new[1:])
  woohoo = round(abs((neww - old1) / old1 * 100))
  if old1 >= neww:
    return str(woohoo) + '%' + ' ' + 'decrease'
  else:
    return str(woohoo) + '%' + ' '+ 'increase'
print(percentage_changed("$100", "$950"))

