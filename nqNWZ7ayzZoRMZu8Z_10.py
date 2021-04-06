
def avg_note(students):
  def format_dict(dic):
    name = dic['name']
    try:
      average = float(round(sum(dic['notes']) / len(dic['notes'])))
    except ZeroDivisionError:
      average = 0
    
    return {'name': name, 'avgNote': average}
  
  return [format_dict(dic) for dic in students]

