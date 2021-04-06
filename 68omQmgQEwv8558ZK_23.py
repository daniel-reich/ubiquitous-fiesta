
# Check the Resources tab for the list of characters and items.
def max_stats(character, gold):
  att = {'Knight':120, 'Warrior':180, 'Fairy':71, 'Robot':160, 'Giant':160}
  dfn = {'Knight':140, 'Warrior':71, 'Fairy':100, 'Robot':120, 'Giant':200}
  spe = {'Knight':6, 'Warrior':8, 'Fairy':16, 'Robot':11, 'Giant':4}
  wea = {20:10, 40:20, 60:30, 80:40, 100:50}
  arm = {30:20, 60:40, 90:60, 120:80, 150:100}
  boo = {24:3, 48:6, 72:9, 96:12, 120:15}
  ans = [0,0,0]
  for i in wea:
    if gold >= i and wea[i]+att[character] > ans[0]:
      ans[0] = wea[i]+att[character]
  for i in arm:
    if gold >= i and arm[i]+dfn[character] > ans[1]:
      ans[1] = arm[i]+dfn[character]
  for i in boo:
    if gold >= i and boo[i]+spe[character] > ans[2]:
      ans[2] = boo[i]+spe[character]
  return ans

