
def describe_num(n):
  adj = ["brilliant", "exciting", "fantastic", "virtuous",  "heart-warming",
  "tear-jerking", "beautiful", "exhillarating", "emotional",  "inspiring"]
  adj_n = ' '.join(a for i,a in enumerate(adj,1) if n%i==0)
  return "The most {} number is {}!".format(adj_n, n)

