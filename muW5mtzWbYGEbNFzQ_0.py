
def BMR(p):
  w,h,a=p['weight'],p['height'],p['age']
  return round((13.75*w+5.003*h-6.755*a+66.47,9.563*w+1.85*h-4.676*a+655.1)[p['gender'][0]=='f']*(1.025+.175*p['sport']),1)

