
def top_note(student):
    name, notes = student['name'], student['notes']
    return {'name':name, 'top_note':max(notes)}

