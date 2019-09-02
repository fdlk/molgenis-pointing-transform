import numpy as np 
import pandas as pd 

from HeaderData import HeaderData

fileName = 'TAB_test_mogenis_2_2019-08-14-160715176 5.tsv'
fileFolder = '/Users/connor/Documents/Projecten/Pointing/sprint141/'
filePath = fileFolder + fileName

print('--- load data ' + fileName + ' ---')

header = HeaderData()

# Read header data
with open(filePath, 'r') as inputFile:
   for line in inputFile:
       print(line)
       header.nHeaderRows += 1
       if line.startswith('Study Name:'):
            header.studyName = line[11:].strip()
       if line.startswith('Study Event Definitions'):
            header.nStudyEventsDefs = line[len('Study Event Definitions'):].strip()
       if line.startswith('Subjects:'):
            header.nSubjects = line[len('Subjects:'):].strip()
       if line in ['\n', '\r\n']:  # check for empty line indicating end of header
            break



print('Number of headerLines: ' + str(header.nHeaderRows))
print('Study name: ' + str(header.studyName))
print('Study Event Definitions: ' + str(header.nStudyEventsDefs))
print('Number of subjects: ' + str(header.nSubjects))