
def champions(teams):
    return max(teams, key=lambda x: (x['wins'] * 3 + x['draws'],
                                     x['scored'] - x['conceded']))['name']

