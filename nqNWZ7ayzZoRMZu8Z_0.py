
def avg_note(students):
    lst = students[0]['notes']
    students[0]['avgNote'] = round(sum(lst) / len(lst)) if lst else 0
    students[0].pop('notes')
    return students

