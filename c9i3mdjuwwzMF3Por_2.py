
def bemirp(num):
 def check_prime(no):
  for n in range(2,int(no**0.5)):
         if (no%n==0):
             return False
  return True
 if not (check_prime(num)):return "C"
 num = str(num)
 if num == num[::-1] or not check_prime(int(num[::-1])):return "P"
 flip=num.replace("6","9").replace("9","6")
 if (check_prime(int(flip)) and check_prime(int(flip[::-1]))): return "B"
 else: return "E"

