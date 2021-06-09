
import json

class FHIRMedicationRequest:

    def __init__(self, patientID=-1):
        self.patientID = patientID
        self.givenName = ""
        self.familyName = ""
        self.gender = ""
        self.birthdate = ""
        self.phone = ""

    def setName(self, givenName, familyName):
        self.givenName = givenName
        self.familyName = familyName

    def setGender(self, gender):
        self.gender = gender
        if self.gender == 'M':
            self.genderDisplay = "Male"
        else:
            self.genderDisplay = "Female"

    def setBirthdate(self, birthdate):
        self.birthdate = birthdate

    def setPhone(self, phone):
        self.phone = phone

    def __str__(self):
        return "Patient " + str(self.patientID)

    def constructJSON(self):
        patientDict = {}
        patientDict["identifier"] = {
                "use": "usual",
                "label": "MRN",
                "system": "example.medical.system",
                "value": self.patientID
                }
        patientDict["name"] = {
                "use": "official",
                "family": [
                    self.familyName
                    ],
                "given": [
                    self.givenName
                    ]
                }
        patientDict["gender"] = {
                "coding": [
                    {
                        "system": "http://hl7.org/fhir/v3/AdministrativeGender",
                        "code": self.gender,
                        "display": self.genderDisplay
                        }
                    ]
                }
        patientDict["birthDate"] = self.birthdate
        patientDict["contact"] = {
                "telecom": {
                    "system": "phone",
                    "value": self.phone
                    }
                }

        return json.dumps(patientDict, indent=4)

    def constructXML(self):
        print(self)
