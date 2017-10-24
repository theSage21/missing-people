import pandas as pd

df = pd.read_csv('data.csv')
mapping = {'NORMAL/MEDIU': 'normalmedium',
           'THIN': 'thin',
           'STRONG': 'strong',
           'FAT': 'fat',
           '2.0NORMAL/MEDIU': 'normalmedium',
           'VERYLANKY(SKELETAL)': 'verylanky',
           '83.0THIN': 'thin',
           '53.0THIN': 'thin',
           'MUSCULAR': 'muscular',
           'VERYFAT': 'veryfat',
           '22.0THIN': 'thin',
           '14.0THIN': 'thin',
           '22.0NORMAL/MEDIU': 'normalmedium',
           '1.0NORMAL/MEDIU': 'normalmedium',
           '1.0THIN': 'thin',
           '83.0NORMAL/MEDIU': 'normalmedium'
           }
df.Built = df.Built.map(mapping)
df.to_csv('cleandata.csv', index=False)
print(df.State.unique())
