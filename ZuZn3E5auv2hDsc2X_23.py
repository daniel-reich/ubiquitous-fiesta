
def longer_than_n_pages(pages):
  books = [
  ('A Very Long Book', 1213),
  ('Short Story: The Short Story', 4),
  ('A Light Read in the Summertime', 43),
  ('An Epic Saga', 617),
  ('The Compelling Narrative', 161),
  ('A Well Rounded Novel', 250),
  ('Introduction to Algorithms', 234) 
]
​
  return [i for i in books if i[1]>pages]

