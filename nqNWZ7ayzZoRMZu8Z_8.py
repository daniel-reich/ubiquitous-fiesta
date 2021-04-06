
def avg_note(students):
    return [{'name': obj['name'], 'avgNote': 0 if not obj['notes'] else round(sum(obj['notes']) / len(obj['notes']))} for obj in students]

