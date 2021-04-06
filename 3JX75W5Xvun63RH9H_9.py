
def describe_num(n):
  adverbs = (
    (1, 'brilliant'),
    (2, 'exciting'),
    (3, 'fantastic'),
    (4, 'virtuous'),
    (5, 'heart-warming'),
    (6, 'tear-jerking'),
    (7, 'beautiful'),
    (8, 'exhilarating'),
    (9, 'emotional'),
    (10, 'inspiring'),
  )
  description = []
  for divisor, adverb in adverbs:
    if n % divisor == 0:
      description.append(adverb)
  return 'The most {} number is {}!'.format(' '.join(description), n)

