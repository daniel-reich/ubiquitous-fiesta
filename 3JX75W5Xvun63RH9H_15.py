
def describe_num(n):
  sentences = [" brilliant", " exciting", " fantastic", " virtuous", " heart-warming", " tear-jerking", " beautiful", " exhilarating", " emotional", " inspiring"]
  sentence = "The most"
  
  for foo in range(1 , 11):
    if n % foo == 0:
      sentence += sentences[foo - 1]
  return sentence + " number is {}!".format(n)

