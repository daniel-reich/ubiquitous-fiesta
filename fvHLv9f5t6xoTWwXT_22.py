
def grab_number_sum(s):
    for c in s:
        if c.isalpha():
            s=s.replace(c," ")
    return sum(map(int, s.split()))

