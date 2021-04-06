
def avg_note(students):
    notes = []
    for student in students:
        avgNote = student['notes']
        if avgNote:
            avgNote = sum(avgNote)/len(avgNote)
        else:
            avgNote = 0
        notes.append({"name": student['name'], "avgNote": round(avgNote)})
    return notes

