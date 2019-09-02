from HeaderData import HeaderData
from HeaderData import StudyEvent
from HeaderData import CaseReportFrom

def readOpenClinHeaderData( filePath):
    header = HeaderData()

    # Read header data
    with open(filePath, 'r') as inputFile:
        for line in inputFile:
            header.nHeaderRows += 1
            if line.startswith('Study Name:'):
                    header.studyName = line[11:].strip()
            elif line.startswith('Study Event Definitions'):
                    header.nStudyEventsDefs = line[len('Study Event Definitions'):].strip()
            elif line.startswith('Subjects:'):
                    header.nSubjects = line[len('Subjects:'):].strip()
            elif line.startswith('Study Event Definition'):
                    eventDefString = line[len('Study Event Definition'):].strip()
                    parts = eventDefString.split() # split on tab
                    studyEvent = StudyEvent()
                    studyEvent.name = str(' '.join(parts[1:-1]))
                    studyEvent.key = str(parts[-1])
                    header.studyEvents.append(studyEvent)
            elif line.startswith('CRF'):
                    splitIndex = line.index('-')
                    leftPart = line[:splitIndex]
                    rightPart = line[splitIndex:]
                    crf = CaseReportFrom()
                    crf.name = ' '.join(leftPart.split()[1:])
                    crf.version = rightPart.split()[1]
                    crf.key = rightPart.split()[-1]
                    header.studyEvents[-1].caseReportFroms.append(crf)

            if line in ['\n', '\r\n']:  # check for empty line indicating end of header
                    break
    return header

def printHeaderData( header):
        print('Number of headerLines: ' + str(header.nHeaderRows))
        print('Study name: ' + str(header.studyName))
        print('Study Event Definitions: ' + str(header.nStudyEventsDefs))
        print('Number of subjects: ' + str(header.nSubjects))

        print('---- Study Events (name, key, crfs(name, verson, key))---- ')
        for studyEvent in header.studyEvents:
                print('   ' + studyEvent.name + ' : ' + studyEvent.key)
                for crf in studyEvent.caseReportFroms:
                        print('       ' + crf.name + ' : ' + crf.version + ' : ' + crf.key)
        return
