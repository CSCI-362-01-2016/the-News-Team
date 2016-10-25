#!/usr/bin/env python
import os
import webbrowser
from project import *

os.chdir("..") #nove back one folder
pathName = str(os.path.dirname(os.path.abspath(__file__)))

def main():
    parseTextFile()

def parseTextFile():
    #number of text files to parse
    txtFileCount = 0

    os.chdir("testCases") #move into the test cases folder

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
    for root, dirs, files in os.walk(pathName):
        if name in files:
            return os.path.join(root, name)
    return

def writeOutputToHtml():
    return;
def textToHtml():
    inf = open("TextForHtml.txt","r")
    outf = open("Output.html","w")
    template = Template("""<!doctype html>

    <html lang="en">
    <head>
      <meta charset="utf-8">

      <title>Files In Directory</title>

    </head>

    <body>
        <h1>The Files In the Directory Are:</h1>
      <p>$output</p>
    </body>
    </html>""")
    files = "";
    for line in inf:
        files += line + "<br>"

    outf.write(template.substitute(output=files))
    inf.close()
    outf.close()

def loadOutputInBrowser():
    return;

main()
