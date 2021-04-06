
def correct_sentences(s):
    import re
    #  res = re.split('(?=[A-Z])', s.strip()) python 3.7
    buf = re.findall('.[^A-Z]*', s.strip())
    res = re.sub(r' +', ' ', ' '.join([x.strip().capitalize() + '.' for x in buf]))
    return res

