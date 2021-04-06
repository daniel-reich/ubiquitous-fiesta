
def add_it_up(lst):
    try:
        return sum(lst)
    except:
        try:
            return sum(lst,[])
        except:
            return sum(lst,())

