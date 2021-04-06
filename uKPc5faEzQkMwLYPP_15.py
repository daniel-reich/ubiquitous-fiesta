
def end_corona(recovers, new_cases, active_cases):
 return int(active_cases / (recovers - new_cases))+1

