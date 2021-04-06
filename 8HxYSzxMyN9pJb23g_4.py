
def split_n_cases(txt, cases):
    if len(txt) % cases != 0:
        return ["Error"]
    return [txt[n:n + int(len(txt)/cases)] for n in range(0, len(txt), int(len(txt)/cases))]

