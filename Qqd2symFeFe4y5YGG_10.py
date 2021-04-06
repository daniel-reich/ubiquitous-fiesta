
def palindromic_date(date):
  d1 = date[:date.find("/")]
  d2 = date[date.find("/")+1:]
  d3 = d2[d2.find("/")+1:]
  d4 = d2[:d2.find("/")]
  d5 = "".join([(d1+d4)[len(d1+d4)-1-i] for i in range(len(d1+d4))])
  d6 = "".join([(d4+d1)[len(d4+d1)-1-i] for i in range(len(d4+d1))])
  return d3 == d5 and d6 == d5

