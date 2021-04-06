
def golf_score(course, result):
    total = 0
    count = 0
    conversion = {"eagle" : -2,"birdie" : -1,"par" : 0,"bogey" : 1,"double-bogey" : 2}
    for elm in result:        
        total = total + (course[count]+conversion[elm])
        count += 1
    return total

