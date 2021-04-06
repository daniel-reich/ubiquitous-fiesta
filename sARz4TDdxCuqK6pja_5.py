
import copy
def deadly_virus(persons, n):
    dict = {}
    for y in range(len(persons)):
        for x in range(len(persons[y])):
            dict[(y,x)] = persons[y][x]
​
    for i in range(n):
        temp = copy.deepcopy(persons)
        for y in range(len(persons)):
            for x in range(len(persons[y])):
                if (y-1,x) in dict:
                    if persons[y-1][x] == 'V':
                        temp[y][x] = 'V'
                if (y+1,x) in dict:
                    if persons[y+1][x] == 'V':
                        temp[y][x] = 'V'
                if (y,x-1) in dict:
                    if persons[y][x-1] == 'V':
                        temp[y][x] = 'V'
                if (y,x+1) in dict:
                    if persons[y][x+1] == 'V':
                        temp[y][x] = 'V'
        persons = copy.deepcopy(temp)
​
    return persons

