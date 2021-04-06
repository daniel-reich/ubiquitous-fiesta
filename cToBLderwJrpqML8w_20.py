
def champions(teams):
    '''
    Returns the champion team based on points gained (and goal difference as a
    tie breaker).
    '''
    return sorted(teams,
                  key=lambda x: (x['wins']*3 + x['draws'],x['scored']-x['conceded']),
                  reverse=True)[0]['name']

