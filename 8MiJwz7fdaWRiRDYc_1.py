
def apocalyptic(n):
    s = str(2**n)
    if '666' in s:
        return "Repent! {} days until the Apocalypse!".format(s.index('666'))
    return "Crisis averted. Resume sinning."

