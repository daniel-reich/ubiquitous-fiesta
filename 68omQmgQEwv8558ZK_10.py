
def max_stats(character, gold):
  lowest_prices_and_increments =  [ [20 , 10] , [30 , 20]  ,[24 , 3]];
  character_to_stats_dict = dict([["Knight" , [120 ,140,6]],
                             ["Warrior" , [180,71,8]],
                             ["Fairy" , [71,100,16]],
                             ["Robot" , [160,120,11]],
                             ["Giant" , [160 ,200,4]]]);
  charcter_stats =  character_to_stats_dict[character];
  return [charcter_stats[idx] + best_equip(gold , *lowest_prices_and_increments[idx] ) for idx in range(0 , len(charcter_stats))]
  
def best_equip(gold , lowest_price , smallest_increment):
  return min(gold//lowest_price , 5) * smallest_increment;

