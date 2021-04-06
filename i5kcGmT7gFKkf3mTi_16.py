
def data_type(value):
    types = {'list':'list','dict':'dictionary','str':'string','int':'integer','float':'float','datetime.date':'date','bool':'boolean'}
    return types.get(str(type(value)).split("'")[1])

