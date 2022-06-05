# %%

import pandas as pd

def read():
    return pd.read_csv("data-sets/olympics.csv", header=1).rename(columns={
        "Unnamed: 0":"country",
        "? Winter":"winter_olympics",
        '? Summer':'summer_olympics',
        '01 !':'summer_golds',
        '02 !':'summer_silvers',
        '03 !':'summer_bronzes',
        'Total':'summer_total',
        'winter_olympics':'winter_olympics',
        '01 !.1':'winter_golds',
        '02 !.1':'winter_silvers',
        '03 !.1':'winter_bronzes',
        'Total.1':'winter_total',
        '? Games':'total_games',
       '01 !.2':'total_golds',
       '02 !.2':'total_silvers',
       '03 !.2':'total_bronzes'   
        })

olympics = read()


# %%
