
import decimal as d
​
def hex_color_mixer(colors):
  hexs = [(x[1:3], x[3:5], x[5:]) for x in colors]
  rgbs = [tuple(map(lambda v: int(v, 16), x)) for x in hexs]
  mix_rgb = [d.Decimal(sum(x) / len(x)).quantize(d.Decimal('1'), rounding=d.ROUND_HALF_UP) for x in zip(*rgbs)]
  mix_hex = [format(int(x), '02x').upper() for x in mix_rgb]
  return '#{}{}{}'.format(*mix_hex)

