
import requests
def is_vampire(n):
  n = str(n)
  pvamp = [x.split()[1] for x in requests.get('https://oeis.org/A020342/b020342.txt').text.splitlines()]
  vamp = [x.split()[1] for x in requests.get('https://oeis.org/A014575/b014575.txt').text.splitlines()]
  return 'True Vampire' if n in vamp else 'Pseudovampire' if n in pvamp else 'Normal Number'#,int(r[n-1].split()[1])

