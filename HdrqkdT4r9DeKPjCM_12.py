
RETURN_FORMAT = '{i}{tail} {k}-gonal number'
​
tail_dict = {
  1: 'st',
  2: 'nd',
  3: 'rd',
  4: 'th',
  5: 'th',
  6: 'th',
  7: 'th',
  8: 'th',
  9: 'th',
  0: 'th',
}
​
# Use a generator to define the sequence for the k-dagonal
def gen_polygonal_sequence(k):
    x = 0
    term = 1
    while True:
        yield term
        x += k
        term += x
​
def is_polygonal(n):
    if n == 1:
        return '0th of all'
    matches = list()
    for k in range(3, n):
        sequence = gen_polygonal_sequence(k)
        term = next(sequence)
        counter = 0 
        while term < n:
            counter += 1
            term = next(sequence)
            if term == n:
                tail = tail_dict[int(str(counter)[-1])]
                if str(counter)[-2:] in ['11', '12', '13']:
                    tail = 'th'
                matches.append(RETURN_FORMAT.format(i=counter, tail=tail, k=k))
    if len(matches) == 0:
        return False
    return(matches)

