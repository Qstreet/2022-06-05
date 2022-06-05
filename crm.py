# %%
import pandas as pd

def read():
    return pd.read_csv("data-sets/CRM-General.csv", low_memory=False).rename(
        columns=lambda header: header.lower().replace(" ", "_")
    )

crm = read()

crm.to_csv("data-sets/crm_header.csv")

# %%
