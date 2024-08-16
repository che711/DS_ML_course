import numpy as np
import pandas as pd

email = 'vlad@email.com'
print(f"email.split('@')")

names = pd. Series(['andrew', 'bobo', 'claire', 'david', '5'])
print(f"\n -> \n{names}")

print(f"\n -> \n{names.str.upper()}")
print(f"\n -> \n{names.str.lower()}")

tech_finance = ['GOOG,APPL,AMZN', 'JPN, BAC,GS']
len(tech_finance)
print(f"\n -> \n{len(tech_finance)}")

tech = 'GOOG,APPL,AMZN'
print(f"\n -> \n{tech.split(',')[0]}")

tickers = pd.Series(tech_finance)
print(f"\n -> \n{tickers.str.split(',', expand=True)}")
print(f"\n -> \n{tickers.str.split(',')}")
print(f"\n -> \n{tickers.str.split(',').str[0]}")

messy_names = pd.Series(['andrew  ', 'bo:bo', '  clair  '])
print(f"\n -> \n{messy_names}")
print(f"\n -> \n{messy_names.str.replace(':', '').str.strip().str.capitalize()}")

def cleanup(name):
    name = name.replace(':', '')
    name = name.strip()
    name = name.capitalize()
    return name


print(f"\nприменяем ф-цию ко всему объекту pd.Series: -> \n{messy_names.apply(cleanup)}")



