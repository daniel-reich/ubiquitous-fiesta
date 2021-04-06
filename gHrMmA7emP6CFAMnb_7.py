
def is_apocalyptic(number):
 occ = str(2**number).count('666')
 return "Safe" if occ==0 else "Single" if occ==1 else "Double" if occ==2 else "Triple"

