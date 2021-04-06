
def security(txt: str) -> str:
  txt = txt.replace('x', '')
  return 'ALARM!' if ('T$' in txt or '$T' in txt) else 'Safe'

