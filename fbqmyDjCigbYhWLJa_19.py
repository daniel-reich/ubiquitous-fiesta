
excl = {'by'}
​
def split_into_buckets(text, limit):
    bucket_words = text.split(" ")
    w_count = len(bucket_words)
    bucket_lst = []
    i = 0
    substring = ""
    while i < w_count:
        prev = substring
        substring += bucket_words[i] + ' '
        i += 1
        if len(substring.rstrip()) > limit:
            if prev and prev.rstrip() not in excl:
                bucket_lst.append(prev.rstrip())
                i -= 1
            substring = ""
    if substring and len(substring.rstrip()) <= limit:
        bucket_lst.append(substring.rstrip())
    return bucket_lst

