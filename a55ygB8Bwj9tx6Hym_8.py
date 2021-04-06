
def steps_to_convert(txt):
    if not txt or txt.isupper() or txt.islower():
        return 0
    else:
        count=sum([1 for i in txt if i.isupper()])
    if count>=len(txt)/2:
        return len(txt)-count
    else:
        return count

