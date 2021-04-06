
def is_icecream_sandwich(txt):
    return len(set(txt))==2 and txt==txt[::-1]

