
def get_xp(d):
    d2={'Very Easy':5,
        'Easy':10,
        'Medium':20,
        'Hard':40,
        'Very Hard':80}
    a=list(d2.values())
    b=list(d.values())
    return str(sum([x*i for x,i in zip(a,b)]))+'XP'

