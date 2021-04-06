
# Helper Function - is prime
def is_prime(num):
 prime=True
 if num > 1:
  for i in range(2,num):
   if num % i == 0:
    prime=False
    break
 else:
  prime=False
 return prime
​
# Helper function - is emirp - prime backwards but no palindrome
def is_emirp(n):
 n_str=str(n)
 n_rev=n_str[-1::-1]
 #print('n_rev ',n_rev)
 if n_str != n_rev and is_prime(int(n_rev)):
  return True
 else:
  return False
 
​
# Function
def bemirp(n):
 # check if prime
 #  else "C"
 if is_prime(n):
  # check if emirp - prime backwards but no palindrome
  #  else "P"
  if is_emirp(n):
   # check if bemirp - then output "B"
   #  else "E"
   # check if contains non-flippable digits
   non_flip=['2','3','4','5','7']
   flippable=True
   for i in range(0,len(str(n))):
    if str(n)[i] in non_flip:
     output="E"
     flippable=False
     break
   #  if not, flip n
   if flippable:
    flip=""
    for k in range(0,len(str(n))):
     if str(n)[k] == '6':
      flip+='9'
     elif str(n)[k] == '9':
      flip+='6'
     else:
      flip+=str(n)[k]
    #print('flip ',flip)
    # if flip is prime
    #  check if emirp
    if is_prime(int(flip)) and is_emirp(int(flip)):
     output="B"    
    else:
     output="E"
  else:
   output="P"  
 else:
  output="C"
 return output

