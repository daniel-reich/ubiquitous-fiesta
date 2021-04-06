
def organize(txt):
  return {'name':txt.split(',')[0],'age':int(txt.split(',')[1]),'occupation':txt.split(',')[2].strip()} if len(txt) > 0 else {}

