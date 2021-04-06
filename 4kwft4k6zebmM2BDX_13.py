
import math
def chi_squared_test(data):
    data['E'].append(sum(data['E']))
    data['T'].append(sum(data['T']))
    data['Tot']=[int(e+t) for e,t in zip(data['E'],data['T'])]
    print(data)
    crossed_data={}
    crossed_data['E']=[(data['E'][2]*i)/data['Tot'][-1] for i in data['Tot'][:-1]]
    crossed_data['T']=[(data['T'][2]*i)/data['Tot'][-1] for i in data['Tot'][:-1]]
    var_data={}
    var_data['E']=[(math.pow(data['E'][i]-crossed_data['E'][i],2)/crossed_data['E'][i]) for i in range(0,2)]
    var_data['T']=[(math.pow(data['T'][i]-crossed_data['T'][i],2)/crossed_data['T'][i]) for i in range(0,2)]
    somme=0
    for key in var_data:
        somme+=sum(var_data[key])
    somme = round(somme,1)
    a1 = 6.635
    a5 = 3.841
    if somme > a1:
        return [somme,"Edabitin effectiveness = 99%"]
    if somme <a1 and somme> a5:
        return [somme,"Edabitin effectiveness = 95%"]
    else:
        return [somme,"Edabitin is ininfluent"]

