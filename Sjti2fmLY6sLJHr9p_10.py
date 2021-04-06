
def sub_sequence(n):
    chars = str(n)
    cur_chars = ""
    seqs = []
    for c in chars:
        if len(cur_chars)==0 or c == cur_chars[-1]:
            cur_chars += c
        else:
            seqs.append(cur_chars)
            cur_chars = c
    seqs.append(cur_chars)
    return seqs
​
def _look_and_say(start, n):
    d = start
    for _ in range(n):
        yield d
        seqs = sub_sequence(d)
        d = ["{}{}".format(len(num), num[0]) for num in seqs]   
        d = "".join(d)    
        d = int(d)
​
def look_and_say(start, n):
  return list(_look_and_say(start, n))

