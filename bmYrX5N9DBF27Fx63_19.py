
def greatest_impact(lst):
    sw,smea,ssl,sm=0,0,0,0
    for i in lst:
       for j in i:
            if i.index(j) == 1:sw += j/10
            if i.index(j) == 2:smea += j / 3
            if i.index(j) == 3:ssl += j / 10
            if i.index(j) == 0:sm += j / 10
    if sw < ssl and sw < smea:return 'Weather'
    elif smea < sw and smea < ssl: return 'Meals'
    elif ssl < sw and ssl < smea : return 'Sleep'
    else : return 'Nothing'

