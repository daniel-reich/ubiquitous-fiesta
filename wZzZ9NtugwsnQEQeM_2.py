
def golf_score(course, result):
    
    dict_result = {'eagle': -2, 'birdie': -1, 'bogey': +1, "double-bogey": +2, 'par': 0}
    
    return sum(x + dict_result.get(y) for x, y in zip(course, result))

