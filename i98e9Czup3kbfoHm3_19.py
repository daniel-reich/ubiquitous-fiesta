
def text_to_number_binary(txt):
    d = {"zero":"0" , "one":"1"}
    no="".join([d[num] for num in txt.lower().split() if num in d.keys()])
    return no[:8*(len(no)//8)]

