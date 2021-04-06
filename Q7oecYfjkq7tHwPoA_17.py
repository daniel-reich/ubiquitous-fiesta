
def climb(s, obs):
    '''
    Returns the number of obstacles in obs which can be cleared with stamina s,
    given the impact on stamina described in the rules.
    '''
    from math import ceil
    '''
    # check how much stamina needed for the full set of obstacles
    print('You need the following stamina to complete the course:')
    tot_stamina = [ceil(abs(b-a))*(2 if b > a else 1) for a,b in zip(obs,obs[1:])]
    print(sum(tot_stamina),'as:',tot_stamina,'\n')
    '''
    
    for i, (a, b) in enumerate(zip(obs, obs[1:])):
        mult = 2 if b > a else 1
        s -= ceil(abs(b-a)) * mult
        #print('a now',a,'b now',b,'s now',s)
        if s < 0:
            return i  # can't include this one
​
    return len(obs) - 1  # cleared them all... but last one doesn't count??

