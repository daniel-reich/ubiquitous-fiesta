
def fizz_buzz(maximum):
  fb_list = []
  for i in range(1, maximum+1):
    if i % 15 == 0:
      fb_list.append('FizzBuzz')
​
    elif i % 5 == 0:
      fb_list.append('Buzz')
​
    elif i % 3 == 0:
      fb_list.append('Fizz')
    
    else:
      fb_list.append(i)
      
  return fb_list

