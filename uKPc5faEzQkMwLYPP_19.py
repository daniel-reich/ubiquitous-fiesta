
def end_corona(recovers, new_cases, active_cases):
 cases=0
 x=0
 dni=0
 cases=int(active_cases)+int(new_cases)-int(recovers)
 x=cases
 while cases>0:
    x=cases
    cases=int(x)+int(new_cases)-int(recovers)
    dni+=1
 return(int(dni)+1)

