
def describe_num(n):
  adj=['brilliant','exciting','fantastic','virtuous','heart-warming','tear-jerking','beautiful','exhillarating','emotional','inspiring']
  return 'The most {} number is {}!'.format(' '.join(adj[i] for i in range(len(adj)) if not n%(i+1)),n)

