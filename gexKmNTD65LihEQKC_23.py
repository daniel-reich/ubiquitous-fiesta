
def is_super_cool(string):
  if not string: return False
  k = len(string)
  lens = [k]
  while True:
    string = read(k)
    if k == len(string): return True
    if len(string) in lens: return False
    k=len(string)
  
read = lambda n: dic1[n] if n<10 else dic2[n] if n<20 else dic3[10*(n//10)] + ' ' + dic1[n%10]
​
dic1 = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
        6:'six', 7:'seven', 8:'eight', 9:'nine'}
dic2 = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 
        15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
dic3 = {20:'twenty', 30:'thirty'}

