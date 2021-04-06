
def split_and_delimit(txt, num, delimiter):
        pattern = [(txt[i:i+num]) for i in range(0, len(txt), num)]
        return delimiter.join(pattern)

