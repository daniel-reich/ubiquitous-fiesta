
from collections import Counter
​
def get_notes_distribution(students):
    ans = {}
    for student in students:
        C = Counter(student["notes"])
        for note, cnt in C.items():
            if 1 <= note <= 5:
                ans[note] = ans.get(note, 0) + cnt
    return ans

