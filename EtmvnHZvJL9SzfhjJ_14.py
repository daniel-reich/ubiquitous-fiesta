
import re
import string
def strip_url_params(url, *params_to_strip):
  for alpha in string.ascii_lowercase:
    pattern = r"({}=)+".format(alpha)
    if len(re.findall(pattern, url)) > 1:
      m = re.search(pattern.format(alpha), url)
      url = url[:m.end()] + re.sub(pattern, "", url[m.end():])
      n = re.search(pattern.format(alpha), url)
      url = url[:n.end()] + url[-1] + url[n.end() + 1:]
      url = url[:-2]
  for param in params_to_strip:
    url = re.sub(r"&{}=[0-9]".format(param), "", url)
    url = re.sub(r"{}=[0-9]&".format(param), "", url)
    url = re.sub(r"{}=[0-9]".format(param), "", url)
  return url

