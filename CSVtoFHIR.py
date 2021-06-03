
from FHIRPatient import FHIRPatient
import sys
import json
import random

SKIP_FIRST_LINE = True
# SKIP_FIRST_LINE = False

PRETTY_PRINT = True
# PRETTY_PRINT = False


def Main():

    if len(sys.argv) < 2:
        csvFilename = "data/default.csv"
    else:
        csvFilename = sys.argv[1]

    csvFileContents = getFileContents(csvFilename)
    csvData = parseCSV(csvFileContents)

    patients = []

    for line in csvData:
        p = FHIRPatient(line[0])
        p.setName(line[1], line[2])
        p.setGender(line[3])
        p.setBirthdate(line[4])
        p.setPhone(line[5])
        patients.append(p)


    for line, patient in zip(csvData, patients):
        print()
        if PRETTY_PRINT:
            print("Patient: " + line[1] + " " + line[2])
            print(line)
            print(patient.constructJSON(), end="\n\n")
        else:
            print(patient.constructJSON(), end="\n")

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
