
def split_into_buckets(phrase, n):
    '''
    Returns a list of the words in phrase split into buckets of max size n as
    per instructions, or an empty ;ist if this is not possible
    '''
    words = phrase.split()
    if len(max(words, key=len)) > n:
        return []
​
    size = len(words)
    i = 0
    buckets = []
    bucket = ''
    space = ''
​
    while i < size:
        while i < size and (len(bucket) + len(space) + len(words[i])) <= n:
            bucket = bucket + space + words[i]
            #print('bucket', bucket, 'length', len(bucket))
            space = ' '
            i += 1
​
        if i < size:
            buckets.append(bucket)
            space = ''
            bucket = ''
            
    if bucket:
        buckets.append(bucket)  #last bucket!
​
    return buckets

