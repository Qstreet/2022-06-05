#from operator import index
# import seaborn as sns
# import matplotlib.pyplot as plt

import pandas as pd
# print(pd.__version__)

### OPTIONS
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)


# def print_full(x):
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', None)
#     pd.set_option('display.width', 2000)
#     pd.set_option('display.float_format', '{:20,.2f}'.format)
#     pd.set_option('display.max_colwidth', None)
#     print(x)
#     pd.reset_option('display.max_rows')
#     pd.reset_option('display.max_columns')
#     pd.reset_option('display.width')
#     pd.reset_option('display.float_format')
#     pd.reset_option('display.max_colwidth')

# def read():
#     return pd.read_csv("data-sets/CRM-General.csv", low_memory=False).rename(
#         columns=lambda header: header.lower().replace(" ", "_")
#     )

def read():
    return pd.read_csv("data-sets/crm_header.csv", low_memory=False)
    #, index_col=[0]

crm = read()

# crm.loc[crm["account_name"].str.contains("USAU")]
# crm.loc[:3,]

# crm.info()

# find cols with number type
# numeric_cols = crm.select_dtypes(include=['number']).columns
# print(numeric_cols)

# find non-number cols
non_numeric_cols = crm.select_dtypes(exclude=['number']).columns
# print(non_numeric_cols)

# get info on non_numerics cols
# crm[non_numeric_cols].info()

# num_missing = crm.isna().sum()
# num_missing[:10]

# plt.figure(figsize=(10,8))

crm_copy = crm.copy()

# Return the most common entry for each non-number column
most_freq = crm_copy[non_numeric_cols].describe().loc['top']
# print(most_freq)

# return rows / records with exact dups
#print(crm_copy[crm_copy.duplicated()])


#print(crm_copy[crm_copy.drop(columns=['contact_id', 'preferred_email']).duplicated()])

print(crm_copy.loc[2066:2067])
# cols = crm.columns[:30]
# colors = ['#000099', '#ffff00'] # specify colours: yellow - missing. blue - not missing
# sns.heatmap(crm[cols].isna(), cmap=sns.color_palette(colors))

# import missingno as msno
# msno.matrix(crm.iloc[:, :30])

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
