
def chi_squared_test(data):
    totPop = sum(data['E'])+sum(data['T'])
    totE = sum(data['E'])
    totT = sum(data['T'])
    twoTot = data['E'][0] + data['T'][0]
    halfTot = data['E'][1] + data['T'][1]
​
    a = ((data['E'][0]-(twoTot*totE/totPop))**2)/(twoTot*totE/totPop)
    b = ((data['E'][1]-(halfTot*totE/totPop))**2)/(halfTot*totE/totPop)
    c = ((data['T'][0]-(twoTot*totT/totPop))**2)/(twoTot*totT/totPop)
    d = ((data['T'][1]-(halfTot*totT/totPop))**2)/(halfTot*totT/totPop)
​
    chiSq = round(a + b + c + d,1)
    myans = [chiSq,'']
    if chiSq > 6.635:
        myans[1] = 'Edabitin effectiveness = 99%'
    elif chiSq > 3.841:
        myans[1] = 'Edabitin effectiveness = 95%'
    else:
        myans[1] = 'Edabitin is ininfluent'
​
    return myans

