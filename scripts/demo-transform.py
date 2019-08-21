import numpy as np 
import pandas as pd 

nHeaderRows = 48
fileName = 'TAB_test_mogenis_2_2019-08-14-160715176 5.tsv'
filePath = '/Users/connor/Documents/Projecten/Pointing/sprint141/' + fileName

print('--- load data ' + fileName + ' ---')


df = pd.read_csv(filePath, sep='\\t', engine='python', skiprows=nHeaderRows, converters={i: str for i in range(1182)})
print(df.info())

# Remove white space from column headers 
df.rename(columns=lambda x: x.strip(), inplace=True)

print('--- read data for table E1_C6 ---')

# Filter column name ends with end with E1_C6 nad copy( allow for white space at the end of the col name)
dfE1C6 = df.filter(regex='.*E1_C6$', axis=1).copy()

# Add 'ID' column to the front of dataframe
dfE1C6.insert(0, 'ID', df.filter(items=['Study Subject ID']))

# Add 'E1-C6' suffix to 'ID' cells
dfE1C6['ID'] = dfE1C6['ID'].astype(str) + '-E1-C6'

dfE1C6.rename(columns=lambda x: x.replace('_E1_C6', ''), inplace=True)

print(dfE1C6.info())

outFile = '/Users/connor/Documents/Projecten/Pointing/sprint141/POI_inclusion_1_1.csv'

dfE1C6.to_csv(outFile, index=False, header=True)

print('--- all done ---')