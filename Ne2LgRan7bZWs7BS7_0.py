
def get_container(product) :
  matches = {'Bread': 'bag', 'Milk': 'bottle', 'Beer': 'bottle', 
             'Eggs': 'carton', 'Cereals': 'box', 'Candy': 'plastic'}
  return matches.get(product)

