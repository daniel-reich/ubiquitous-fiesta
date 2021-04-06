
def lcm(nums):
  answer = 1
  for i in nums:  
      answer = int((answer * i)/gcd(answer, i)) 
  return answer
      
def gcd(a,b):
  return a if(b==0) else gcd(b,a%b)

