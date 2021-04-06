
def afterNMonths(year,month):
  if year != None and month != None: return (year * 12 + month)//12
  if year == None: return "year missing"
  else: return "month missing"

