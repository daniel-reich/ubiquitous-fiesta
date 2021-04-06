
def BMR(person):
    a=655.1 + (9.563*person['weight']) + (1.85 * person['size'])-(4.676 * person['age'])
    b=(66.47 + (13.75*person['weight']) + (5.003*person['size'])-(6.755 *person['age']))
    if person["gender"]=='female' and person['sport']==5:
        return round((a*1.9),1)
    if person["gender"]=='female' and person['sport']==2:
        return round((a*1.375),1)
    if person["gender"]=='male' and person['sport']==2:
        return round((b*1.375),1)
    if person["gender"]=='male' and person['sport']==3:
        return round((b*1.55),1)

