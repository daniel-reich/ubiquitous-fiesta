
def hex_color_mixer(colors):
  red_hex  = mix_colors([color.replace("#" ,"")[:2] for color in colors]);
  green_hex  = mix_colors([color.replace("#" ,"")[2:4] for color in colors]);
  blue_hex  =  mix_colors([color.replace("#" ,"")[4:6] for color in colors]);
  return "#{0}{1}{2}".format(red_hex , green_hex , blue_hex );
​
  
def mix_colors(colors):
  mean  = sum([int(color,16) for color in colors])/len(colors);
  return hex(int(mean + 0.5))[2:].zfill(2).upper();

