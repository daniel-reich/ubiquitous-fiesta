
def get_notes_distribution(students):
    distribution = dict()
    for student in students:
        for note in student['notes']:
            if 0 < note < 6:
                if note in distribution:
                    distribution[note] += 1
                else:
                    distribution[note] = 1
    return distribution

