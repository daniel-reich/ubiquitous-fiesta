
def get_xp(d):
    xp_dict = {'Very Easy' : 5,
               'Easy' : 10,
               'Medium' : 20,
               'Hard' : 40,
               'Very Hard' :80}
    return str(sum([xp_dict[i] * d[i] for i in d.keys()])) + 'XP'

