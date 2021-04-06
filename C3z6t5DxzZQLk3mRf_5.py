
def tune(notes):
    '''
    Returns a list of how closely the notes in notes match the required
    frequencies as described in the instructions.
    '''
​
    TARGET = (329.63, 246.94, 196.00, 146.83, 110.00, 82.41) # freq sequence
​
    def check(target, played):
        '''
        Checks note played against target and returns an assessment string as
        described in the instructions.
        '''
        if played == 0:
            return ' - '
        
        gap = abs(target - played) / target * 100 # % difference
        if gap < 0.5:  # pure guesswork in the absence of tolerance info!!
            return 'OK'
        
        direction = '>' if played < target else '<'
        mag = 1 if gap < 2.5 else 2
​
        return direction * mag + '+' if direction == '>' else \
               '+' + direction * mag
​
    return [check(a, b) for a, b in zip(TARGET, notes)]

