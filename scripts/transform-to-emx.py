import numpy as np 
import pandas as pd 

import headerService
import tableService

fileName = 'TAB_test_mogenis_2_2019-08-14-160715176 5.tsv'
fileFolder = '/Users/connor/Documents/Projecten/Pointing/sprint141/'
outPutFolder = '/Users/connor/Documents/Projecten/Pointing/sprint142/'
molgenisGroupPrefix = 'POI_'

filePath = fileFolder + fileName

print('--- load data ' + fileName + ' ---')

header = headerService.readOpenClinHeaderData(filePath)
headerService.printHeaderData(header)

df = pd.read_csv(filePath, sep='\\t', engine='python', skiprows=header.nHeaderRows, converters={i: str for i in range(1182)})
print(df.info())

# Remove white space from column headers 
df.rename(columns=lambda x: x.strip(), inplace=True)

# Use header data to create separate out files for each case report form
for studyEvent in header.studyEvents:
                print('   ' + studyEvent.name + ' : ' + studyEvent.key)
                for crf in studyEvent.caseReportFroms:
                        print('       ' + crf.name + ' : ' + crf.version + ' : ' + crf.key)
                        outTable = tableService.transformTable(df, studyEvent.key + '_' + crf.key)
                        molgenisTableName = crf.name
                        outFile = outPutFolder + molgenisGroupPrefix + molgenisTableName + '.csv'
                        outTable.to_csv(outFile, index=False, header=True)


print('--- All done, output at: ' + outPutFolder + ' ---')