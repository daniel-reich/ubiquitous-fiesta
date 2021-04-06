
def num_of_leapyears(years):
  return (len([x for x in range(int(years[:years.find("-")]),int(years[years.find("-")+1:])+1) if ( x % 4 == 0 and x % 100 != 0 or x % 400 == 0 ) ]))

