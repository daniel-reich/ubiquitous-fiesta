
def remove_special_characters(txt):
    from string import punctuation
    from re import sub
    rep = "[{stg}]".format(stg=sub("[-_ ]", "", punctuation))
    return (sub(rep, "", txt))

