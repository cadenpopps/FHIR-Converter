import random
import json

class FHIRCondition:

    def __init__(self):
        self.code = None
        self.clinicalStatus = None
        self.verificationStatus = None
        self.subject = None
        self.recordedDate = None

    def setCode(self, conditionID, conditionDisplayName):
        self.code = {
                "system": "https://icdlist.com/icd-10",
                "code": str(conditionID),
                "display": conditionDisplayName
                }

    def setSubject(self, subjectDisplayName):
        self.subject = {
                "reference": "InternalPatientList/p" + str(random.randint(100,999)),
                "display": subjectDisplayName
                }

    def setVerificationStatus(self, verificationStatus):
        self.verificationStatus = verificationStatus

    def setClinicalStatus(self, clinicalStatus):
        self.clinicalStatus = clinicalStatus

    def setRecordedDate(self, recordedDate):
        self.recordedDate = recordedDate

    def __str__(self):
        return "Condition " + self.code[display]

    def constructJSON(self):
        dictionaryRepresentation = vars(self)
        return json.dumps(dictionaryRepresentation, indent=4)

    def constructXML(self):
        print(self)
