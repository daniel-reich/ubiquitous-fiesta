
def avg_note(students):
    return [{'name':i['name'],'avgNote':0 if not i['notes'] else round(sum(i['notes'])/len(i['notes']))} for i in students]

