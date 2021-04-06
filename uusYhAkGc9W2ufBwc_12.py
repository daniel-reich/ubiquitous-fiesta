
def system_escape_velocity(planet):
    i = Ve = Ratio = 0
    k, vEarth = .2929, 16.6
    PD = {'Mercury':[4.25,67.7], 'Venus':[10.36,49.5],'Earth':[11.186,42.1],'Mars':[5.03,34.1],
  'Jupiter':[60.20,18.5],'Saturn':[36.09,13.6],'Uranus':[21.38,9.6],'Neptune':[23.56,7.7]}
    for i in PD:
        if i == planet:
            rtplan = PD[i]
            Ve =  ((PD[i][0]** 2) + (k* PD[i][1])**2)** .5
            Ratio = (Ve/vEarth)
            break
        else:
            continue
    string = "The escape velocity from the system {0}/Sun is {1:.1f} km/s.\nThe escape velocity from the system {0}/Sun is {2:.1f} times the escape velocity from the system Earth/Sun."
    return string.format(i,Ve,Ratio)

