
def max_occur(text):
  counts = {ch:text.count(ch) for ch in set(text)}
  if len(set(counts.values())) == 1:
    return 'No Repetition'
    
  m_count = max(counts.values())
  return [k for k, v in counts.items() if v == m_count]

