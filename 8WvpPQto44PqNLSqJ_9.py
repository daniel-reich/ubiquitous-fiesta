
def pad(message):
    message = message if len(message)%2 else message + ' '
    return (message + 'lo'*70)[:140]

