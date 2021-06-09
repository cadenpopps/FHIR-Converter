
from FHIRPatient import FHIRPatient
from FHIRCondition import FHIRCondition
from FHIRProcedure import FHIRProcedure
from FHIRMedicationRequest import FHIRMedicationRequest
import sys

SKIP_FIRST_LINE = True
# SKIP_FIRST_LINE = False

PRETTY_PRINT = True
# PRETTY_PRINT = False


def Main():

    if len(sys.argv) < 2:
        csvFilename = "data/six_patients.csv"
    else:
        csvFilename = sys.argv[1]

    csvFileContents = getFileContents(csvFilename)
    csvData = parseCSV(csvFileContents)

    resources = convertResourcesToFHIR(csvData)


    for line, resource in zip(csvData, resources):
        print()
        if PRETTY_PRINT:
            print("CSV")
            print(line)
            print("FHIR")
            print(resource, end="\n\n")
        else:
            print(resource, end="\n")

    return 0


def getFileContents(filename):
    fileContents = ""
    with open(filename, "r") as f:
        fileContents = f.read()
    return fileContents

def parseCSV(csvContents):
    csvLines = csvContents.splitlines()

    for lineNum in range(0, len(csvLines)):
        csvLines[lineNum] = parseLine(csvLines[lineNum])


    if SKIP_FIRST_LINE:
        return csvLines[1:]
    else:
        return csvLines

def parseLine(csvLine):
    csvElements = csvLine.split(",")
    return csvElements

def convertPatientToFHIR(patientData):
    patient = FHIRPatient(patientData[1])
    patient.setName(patientData[2], patientData[3])
    patient.setGender(patientData[4])
    patient.setBirthdate(patientData[5])
    patient.setPhone(patientData[6])
    return patient.constructJSON()

def convertConditionToFHIR(conditionData):
    condition = FHIRCondition()
    condition.setCode(conditionData[1], conditionData[2])
    condition.setClinicalStatus(conditionData[3])
    condition.setVerificationStatus(conditionData[4])
    condition.setSubject(conditionData[5])
    condition.setRecordedDate(conditionData[6])
    return condition.constructJSON()

def convertProcedureToFHIR(procedureData):
    procedure = FHIRProcedure()
    return procedure.constructJSON()

def convertMedicationToFHIR(medicationData):
    medication = FHIRMedicationRequest()
    return medication.constructJSON()

def convertResourcesToFHIR(csvData):
    resources = []
    for line in csvData:
        resources.append(convertToFHIR[line[0]](line))
    return resources


convertToFHIR = {
        "Patient": convertPatientToFHIR,
        "Condition": convertConditionToFHIR,
        "Procedure": convertProcedureToFHIR,
        "Medication": convertMedicationToFHIR
        }

Main()
