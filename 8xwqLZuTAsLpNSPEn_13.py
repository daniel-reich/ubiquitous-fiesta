
def award_prizes(d):
    s_d = sorted(d.values())[-3:][::-1]
    medals = ['Gold','Silver','Bronze']
    d_medals = {a:medals.pop(0)  for a in s_d}
    for k,v in d.items():
        if v in d_medals:
            d[k] = d_medals[v]
        else:
            if not v in d_medals:
                d[k] = 'Participation'
    return d

