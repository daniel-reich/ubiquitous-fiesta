
def monkey_talk(x):
    y = " ".join(i.replace(i,'eek') if i.startswith('e') or i.startswith('i') or i.startswith('a') else i.replace(i,'ook') for i in x.lower().split())
    return y.capitalize()+'.'

