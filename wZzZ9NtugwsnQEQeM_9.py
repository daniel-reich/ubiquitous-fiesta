
def golf_score(course, result):
        return sum(map(lambda x: -2 if x == 'eagle' else (-1 if x == 'birdie' else (1 if x == 'bogey' else (2 if x == 'double-bogey' else 0))), result)) + sum(course)

