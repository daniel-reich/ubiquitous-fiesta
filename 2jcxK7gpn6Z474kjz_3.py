
def security(txt):
    alert = any(i in txt.replace('x', '') for i in ('T$', '$T'))
    return 'ALARM!' if alert else 'Safe'

