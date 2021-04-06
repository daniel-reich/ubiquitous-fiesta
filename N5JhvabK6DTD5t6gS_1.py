
def markdown(c):
    def format_string(s, w):
        return ' '.join([c+x+c if w.lower() in x.lower() else x for x in s.split()])
    return format_string

