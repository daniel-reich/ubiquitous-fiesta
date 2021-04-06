
def award_prizes(names):
    d={}
    x=sorted(names.values())[-3:]
    for i in names.keys():
        if names[i]==x[-1]:
            d[i]='Gold'
        elif names[i]==x[1]:
            d[i]='Silver'
        elif names[i]==x[0]:
            d[i]='Bronze'
        else:
            d[i]="Participation"
    return d

