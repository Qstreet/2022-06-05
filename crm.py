# %%

from operator import index
import pandas as pd
# print(pd.__version__)

### OPTIONS
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')

# def read():
#     return pd.read_csv("data-sets/CRM-General.csv", low_memory=False).rename(
#         columns=lambda header: header.lower().replace(" ", "_")
#     )

def read():
    return pd.read_csv("data-sets/crm_header.csv", low_memory=False,index_col=[0])

crm = read()

crm.loc[crm["account_name"].str.contains("USAU")]
# crm.loc[:3,]

# crm.rename(columns= \ 
#   {"preferredphone": "preferred_phone", "officephone": "office_phone","homephone":"home_phone"}, \
#   inplace=True)

# %%
#crm.to_csv('crm_out.csv', index=False)
#crm['educational_background'].describe
# val = crm['educational_background']
# print_full(val)


# %%
# crm['educational_background'].isnull().sum()
#.values().any()




# %%
