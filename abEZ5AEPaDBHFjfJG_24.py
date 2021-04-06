
def formula(txt):
  formula_chunks = txt.replace(' ', '').replace('a', '4').split('=')
  chunk_iter = iter(formula_chunks)
  first_chunk = next(chunk_iter)
  try:
    while txt:
      result = eval(first_chunk) == eval(next(chunk_iter))
      if not result: return result
    return None
  except StopIteration:
    return result

