
def get_languages(num):
  a={1:"C#",2:"C++",4:"Java",8:"JavaScript",16:"PHP",
  32:"Python",64:"Ruby",128:"Swift"}
  return sorted(a[i] for i in a if i&num!=0)

