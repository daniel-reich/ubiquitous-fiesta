
soroban = lambda f: int(''.join([str(i[:2].index('O') * 5 
                  + i[3:].index('|')) for i in list(zip(*f))]))

