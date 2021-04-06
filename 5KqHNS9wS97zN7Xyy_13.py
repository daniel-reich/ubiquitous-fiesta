
def top_note(student):
    student['top_note'] = max(student['notes'])
    del student['notes']
    return student

