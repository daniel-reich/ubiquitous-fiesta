
def bar_chart(results):
    d=sorted(sorted(results.items()),key=lambda x:x[1],reverse=True)
    return '\n'.join([x[0]+'|'+'#'*(x[1]//50)+(' ' if x[1] else '')+str(x[1]) for x in d])

