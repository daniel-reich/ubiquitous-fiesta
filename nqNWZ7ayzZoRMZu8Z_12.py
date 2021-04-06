
def avg_note(students):
    from statistics import mean
    return [{'name': x['name'], 'avgNote': 0 if len(x['notes']) == 0
    else round(mean(x['notes']))} for x in students]

