
def first_before_second(tekst,first,second):
    try:
        tekst.index(first,tekst.find(second))
        return False
    except: return True

