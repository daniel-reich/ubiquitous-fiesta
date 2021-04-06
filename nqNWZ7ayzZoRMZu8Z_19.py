
def avg_note(lst):
    return [dict(name = i['name'], avgNote = round(sum(i['notes'])/len(i['notes'])) if len(i['notes']) > 0 else 0)
             for i in lst]

