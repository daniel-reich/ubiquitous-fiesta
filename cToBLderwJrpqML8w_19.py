
def champions(teams):
    return sorted([[i['wins']*3 + i['draws'], i['scored']-i['conceded'], i['name']] for i in teams])[-1][-1]

