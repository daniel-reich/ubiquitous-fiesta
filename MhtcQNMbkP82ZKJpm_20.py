
def get_notes_distribution(students):
    together = [x["notes"] for x in students]
    note = [i for j in together for i in j if 0 < i < 6]
    return {i : note.count(i) for i in set(note)}

