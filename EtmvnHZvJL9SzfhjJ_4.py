
def strip_url_params(url, exclude = []):
  if "?" not in url:
    return url
  base, params = url.split("?")
  params = dict(x.split("=") for x in params.split("&"))
  params = [(k, params[k]) for k in sorted(params) if k not in exclude]
  return base + "?" + "&".join("=".join(x) for x in params)

