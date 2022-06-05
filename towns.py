# %%

import pandas as pd

def read():
    return pd.read_csv("towns.csv", index_col=0)

# def read():
#     towns = []
#     state = ""

#     with open("data-sets/university_towns.txt", mode='r') as file:
#         for line in file:
#             if "[edit]" in line:
#                 state = line.strip()
#             else:
#                 towns.append([state, line])

#     return pd.DataFrame(towns, columns=["state","town"])
    

towns = read()

# towns.to_csv("towns.csv")



# %%
