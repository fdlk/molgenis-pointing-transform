class HeaderData:
    def __init__(self):
        self.studyName = ''
        self.nHeaderRows = 0
        self.nStudyEventsDefs = 0
        self.nSubjects = 0
        self.studyEvents = []

class StudyEvent:
    def __init__(self):
        self.name = ''
        self.key = '' # En for example: E1 or E12 
        self.caseReportFroms = []

class CaseReportFrom:
    def __init__(self):
        self.name = ''
        self.version = 0.0
        self.key = '' # En for example: E1 or E12 
