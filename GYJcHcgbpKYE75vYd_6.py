
def return_end_of_number(num):
    d = {'1':'-ST',
         '2':'-ND',
         '3':'-RD',}
    s = str(num)
    if s[-2:] in ('11', '12', '13'):
        return s + '-TH'
    return s + d.get(s[-1], '-TH')

