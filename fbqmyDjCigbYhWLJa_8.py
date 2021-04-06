
def split_into_buckets(phrase, n):
    if type(phrase) != str or type(n) != int:
        return 'Error: Invalid parameter type!'
​
    else:
        words = phrase.split() # split string into words
        numWords = len(words) # get length before changing var
        wordBuckets = []
        bucketedWords = []
​
        for (i, word) in enumerate(words):
            # if any of the words are
            # too big to be 'bucketized'
            # return []
            if len(word) > n:
                return []
​
            # only create bucket if the
            # word has not already been
            # 'bucketized'
            elif (i, word) not in bucketedWords:
                j = i # make a copy of counter
​
                # while loop condition
                # string of words that
                # can be grouped into
                # a 'bucket' of size n
                wordBucket = []
                wordBucketLen = 0
​
                while j < numWords and wordBucketLen <= n:
                    # metadata for where the word
                    # was found to exclude
                    # duplicate words
                    word = words[j]
​
                    bucketedWords.append((j, word))
                    wordBucket.append(word)
​
                    # length word bucket joined by
                    # whitespace + length of next
                    # word + extra whitespace
                    # only calculate when j
                    # is not the last index
                    # to avoid error
                    if j != (numWords - 1):
                        wordBucketLen = len(' '.join(wordBucket)) + len(words[j + 1]) + 1
​
                    j += 1 # increment
​
                wordBucket = ' '.join(wordBucket) # join to string
                wordBuckets.append(wordBucket)
​
        return wordBuckets

