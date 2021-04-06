
def determine_who_cursed_the_most(d):
    me = []
    wife =[]
    for k in d.keys():
        me.append(d[k]['me'])
        wife.append(d[k]['spouse'])
    return 'DRAW!' if sum(me)==sum(wife) else 'spouse!'.upper() if sum(wife)>sum(me) else 'ME!'

