
def replace(txt, r):
    rr = [chr(i) for i in range(ord(r[0]), ord(r[2])+1)]
    return "".join(['#' if i in rr else i for i in txt])

