import pandas as pd

def read():
    towns = []
    state = ""
    with open("data-sets/bubbles.txt", mode="r") as file:
        for line in file:
            state = line.strip()
            towns.append([state, line])
            
    return towns

towns = read()

print(towns)