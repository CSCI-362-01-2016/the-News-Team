#!/usr/bin/env python
import os
import webbrowser

pathName = str(os.path.dirname(os.path.abspath(__file__)))

def main():
    parseTextFile()

def parseTextFile():
    #number of text files to parse
    txtFileCount = 0

    os.chdir("..") #nove back one folder
    print(os.getcwd())
    os.chdir("testCases") #move into the test cases folder
    os.listdir(os.getcwd())

    #gathering count of test case files
    for file in os.listdir(os.getcwd()):
        # dataList in the form of
        # [0] Test number
        # [1] Requirement being tested
        # [2] Component being tested
        # [3] Method being tested
        # [4] Test input
        # [5] Expected Outcomes
        dataList = []

        if file.endswith(".txt"):
            txtFileCount += 1

            inputFile = open(file, "r")
            for line in inputFile:
                dataList.append(line)
            inputFile.close()

            print ("Data list for text file #" + str(txtFileCount))
            print(dataList)
            print("\n")


def executeTestCase():
    return;

def writeOutputToHtml():
    return;

def loadOutputInBrowser():
    return;

main()