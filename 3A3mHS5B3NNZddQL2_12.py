
def interview(answers, time):
    '''
    Returns 'qualified' if the answers and time meet the passing criteria,
    otherwise 'disqualified'
    '''
    TIME, NUM_Q, LIMITS = 120, 8, [5,5,10,10,15,15,20,20]
​
    outcome = time <= TIME and len(answers) == NUM_Q and \
           all(answer <= LIMITS[i] for i, answer in enumerate(answers))
    return ('disqualified','qualified')[outcome]

