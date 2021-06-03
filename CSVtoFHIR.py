
from FHIRPatient import FHIRPatient
import sys
import json
import random

SKIP_FIRST_LINE = True
# SKIP_FIRST_LINE = False

# INCLUDE_EMPTY_FIELDS = True
INCLUDE_EMPTY_FIELDS = False

def Main():

    if len(sys.argv) < 2:
        print("Please provide filename as such: python HL7Parser.py filename")
        return 0

    csvFilename = ""
    outputFilename = "defaultOut.json"

    csvFileContents = getFileContents(sys.argv[1])
    csvData = parseCSV(csvFileContents)

    patients = []

    for line in csvData:
        # p = FHIRPatient(random.randint(10000, 1000000))
        p = FHIRPatient(line[0])
        p.setName(line[1], line[2])
        p.setGender(line[3])
        p.setBirthdate(line[4])
        p.setPhone(line[5])
        patients.append(p)

    for patient in patients:
        print(patient.constructJSON(), end="\n\n")

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


Main()
