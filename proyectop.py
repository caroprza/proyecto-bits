import pandas as pd
df = pd.read_csv('datachida.csv', sep=';', encoding='latin1')
print(df['bits'].min())
