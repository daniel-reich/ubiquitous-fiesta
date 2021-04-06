
def who_passed(students):
​
    names = []
    for key, value in students.items():
        x1 = [i.split('/') for i in value]
        x2 = [[int(i) for i in x] for x in x1] 
        
        if sum([True if i[0]==i[1] else False for i in x2]) == len(x2):
            names += [key]
​
    return sorted(names)

