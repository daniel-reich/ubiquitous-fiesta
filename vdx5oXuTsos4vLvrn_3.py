
def kaprekar_numbers(p, q):
  kns = []
  for n in range(p, q+1):
    sqs, d = str(n*n), len(str(n))
    if int(sqs[-d:]) + (int(sqs[:-d]) if len(sqs) > 1 else 0) == n:
      kns.append(str(n))
  return ' '.join(kns) if kns else 'INVALID RANGE'

