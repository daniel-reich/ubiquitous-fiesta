
def ecg_seq_index(num):
  ECG_seq  = [1,2];
  while (ECG_seq[-1] != num):
    last_elem  = ECG_seq[-1];
    last_elem_divs  = get_divs(last_elem);
    current = 2;
    while(True):
      current+=1;
      if (current in ECG_seq):
        continue;
        
      current_divs  = get_divs(current);
      if (len(set(last_elem_divs) & set(current_divs)) >= 1):
        ECG_seq.append(current);
        break;
        
  return len(ECG_seq)-1;
​
​
def get_divs(number):
  return [k for k in range(2,number+1) if number%k==0 ];

