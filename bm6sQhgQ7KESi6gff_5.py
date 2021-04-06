
def find_the_difference(s, t):
    for x,y in zip(sorted(s)+[" "], sorted(t)):
        if x!=y:
            return y

