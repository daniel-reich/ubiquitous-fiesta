
def valid_division(d):
 listt=d.split('/')
 if int(listt[1])==0:
   return 'invalid'
 else:
   return int(listt[0])%int(listt[1])==0

