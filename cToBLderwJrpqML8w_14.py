
def champions(teams):
    return sorted([(i['name'], i['wins']*3+i['draws'], i['scored']-i['conceded']) for i in teams], key = lambda x: x[1:3], reverse = True)[0][0]

