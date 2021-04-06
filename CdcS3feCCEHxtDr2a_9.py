
import pandas as pd
def clear_ordering(lst):
    tpl = pd.DataFrame(list(set([tuple(i) for i in lst])))
    tpl = tpl.rename(columns={0: 'Previous', 1: 'After'})
    s = tpl.shape[0] - tpl['Previous'].isin(tpl['After']).sum() + \
        tpl.shape[0] - tpl['After'].isin(tpl['Previous']).sum()
    return tpl['Previous'].shape[0] == tpl['Previous'].unique().shape[0] and \
            tpl['After'].shape[0] == tpl['After'].unique().shape[0] and s == 2

