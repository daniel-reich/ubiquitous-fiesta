
def split_into_buckets(phrase, n):
    words = phrase.split()
    
    result = []
    
    i = 0
    start = 0
    
    count = len(words[i])
    
    if count > n:
        return []
    else:
        while True:
            i += 1
            count = len(' '.join(words[start:i]))
            if count > n:
                i -= 1
                result.append(' '.join(words[start:i]))
                start = i
            elif i == len(words):
                result.append(' '.join(words[start:i]))
                return result

