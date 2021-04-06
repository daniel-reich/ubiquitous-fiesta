
strip_url_params=lambda u,p=[]:u[:19]+'&'.join('='.join(i)for i in sorted(dict(tuple(x.split('='))for x in u[19:].split('&')if u[19:]).items())if i[0]not in p)

