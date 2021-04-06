
def encryption(message):
    message=message.replace(' ','')
    g=int((len(message)**0.5)//1+1)
    return ' '.join([message[n::g] for n in range(0,g)])

