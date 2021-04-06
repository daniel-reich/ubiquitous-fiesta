
def markdown(s):
    def func(string, pattern):
        return ' '.join([x if pattern.lower() not in x.lower() else '{}{}{}'.format(s,x,s) for x in string.split()])
    return func

