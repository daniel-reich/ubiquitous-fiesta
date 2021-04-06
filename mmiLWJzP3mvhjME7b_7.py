
FSA = {
       'S0': {0: 'S0', 1: 'S1'},
       'S1': {0: 'S2', 1: 'S0'},
       'S2': {0: 'S1', 1: 'S2'}
       }  # the finite state machine
​
def divisible(command, state='S0'):
    
    def helper(p):
        return divisible(p, FSA[state].get(command, state))
        
    return state if command == 'state' else 'accept' if command == 'stop' \
           and state == 'S0' else 'reject' if command == 'stop' \
           and state != 'S0' else helper

