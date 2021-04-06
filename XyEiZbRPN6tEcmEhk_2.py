
def height(side):
    return str(round(side*(3**0.5)/2,2)).replace('.','')[0:2]+'.'+str(round(side*(3**0.5)/2,2))[-1]+' mm' if len(str(round(side*(3**0.5)/2,2)))==4 else str(round(side*(3**0.5)/2,2)).replace('.','')[0:3]+'.'+str(round(side*(3**0.5)/2,2))[-1]+' mm'

