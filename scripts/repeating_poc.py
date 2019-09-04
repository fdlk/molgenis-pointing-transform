import numpy as np 
import pandas as pd 
import re

fileName = 'TAB_test_mogenis_2_2019-08-26-150618958.tsv'
fileFolder = './input/'
outPutFolder = './output/'
molgenisGroupPrefix = 'POI_'

filePath = fileFolder + fileName

print('--- load data ' + fileName + ' ---')

# TODO: add na_values?
df = pd.read_csv(filePath, sep='\\t', engine='python', skiprows=48, converters={i: str for i in range(1182)})
df.rename(columns=lambda x: x.strip(), inplace=True)
print(df.info())
print(df.columns)

# Split column header into its parts:
# Variable name, experiment number, experiment repeat number, crf number, crf repeat number 
variable_regex = re.compile(r"(\w+)_((E\d+)(_(\d+))?_(C\d+)(_(\w+))?)")
melted = df.melt(id_vars=['Study Subject ID', 'Protocol ID']).dropna()
melted['varname'] = melted['variable'].apply(lambda variable: variable_regex.match(variable).group(1))
melted['ID'] = melted['Study Subject ID'] + '_' + melted['variable'].apply(lambda variable: variable_regex.match(variable).group(2))
melted['exp'] = melted['variable'].apply(lambda variable: variable_regex.match(variable).group(3))
melted['exp_repeat'] = melted['variable'].apply(lambda variable: variable_regex.match(variable).group(5))
melted['crf'] = melted['variable'].apply(lambda variable: variable_regex.match(variable).group(6))
melted['crf_repeat'] = melted['variable'].apply(lambda variable: variable_regex.match(variable).group(8))

# exps = melted.groupby(['Study Subject ID', 'exp', 'crf', 'ID']).count()
# for key in exps:
#     (subject, exp, crf, id) = key
#     print(subject, exp, crf, id)

# Data for root table


# Data for experiment table E1
e1 = melted[melted['exp']=='E1'][melted['crf_repeat'].isna()].groupby(['Study Subject ID', 'crf', 'ID'], as_index=False).first()
e1.pivot(columns='crf', values='ID', index='Study Subject ID')

# Count the repeats
melted.groupby(['exp', 'crf']).nunique()[['exp_repeat', 'crf_repeat']]


# Data for repeated values E3_C12
# N.B. E3 AND C12 both have repeated parts!
e3c12 = melted[melted['exp']=='E3'][melted['crf']=='C12'][melted['crf_repeat'].notna()].pivot(columns='varname', values='value', index='ID')

e3c12 = melted[melted['exp']=='E3'][melted['crf']=='C12'][melted['crf_repeat'].isna()].pivot(columns='varname', values='value', index='ID')

# e.g. experiment E1, crf C7, skip the repeats
melted[melted['exp'] == 'E1'][melted['crf'] == 'C7'][melted['crf_repeat'].isna()].pivot(columns='varname', values='value', index='ID')

melted[melted['exp'] == 'E1'][melted['crf'] == 'C7'][melted['crf_repeat'].notna()].pivot(columns='varname', values='value', index='ID')