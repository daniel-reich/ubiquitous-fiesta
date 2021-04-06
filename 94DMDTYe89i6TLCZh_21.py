
def get_languages(num):
  di = {1: "C#" ,2: "C++",  4: "Java",8: "JavaScript",  16: "PHP",32: "Python",64: "Ruby",128: "Swift",}
  result = []
  for i in [128,64,32,16,8,4,2,1]:
    if num % i != num:
      result.append(di[i])
      num = num % i
  return sorted(result)

