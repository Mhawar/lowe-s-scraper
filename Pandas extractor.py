import pandas as pd

df = pd.read_csv('Promocode.csv')

List = df['Promo code'].to_list()

print(List)