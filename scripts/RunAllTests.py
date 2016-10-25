#!/usr/bin/env python
import os
import webbrowser
from string import Template


os.chdir("..") #nove back one folder
pathName = str(os.path.dirname(os.path.abspath(__file__)))

def main():
    parseTextFile()
    formatList =["Test case","requirement","component","method","inputs","expected outcome(s)","actual outcome","PASS/FAIL","Test case","requirement","component","method","inputs","expected outcome(s)","actual outcome","PASS/FAIL"]
    textToHtml(formatList)
    loadOutputInBrowser()

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
def textToHtml(listOutput):
    outf = open("TestReport.html","w")
    template = Template("""<!doctype html>

    <html lang="en">
    <head>
      <meta charset="utf-8">

      <title>Test Report</title>

    </head>

    <body>
        <h1>Test Output</h1>
      <p>$output</p>
    </body>
    </html>""")
    out = "";
    index = 0;
    formatList =["Test case","Requirement","Component","Method","Inputs","Expected outcome(s)","Actual outcome","PASS/FAIL"]
    while index < len(listOutput)-2:
        out += "<dl>"
        for i in range(0,8):
            out = out + "<dt>" +formatList[i]
            out = out + "<dd>" +listOutput[index] + "</dd>" + "</dt>"
            index += 1
        out += "</dl>"

    outf.write(template.substitute(output=out))
    outf.close()

def loadOutputInBrowser():
    new = 2  # Code used to open html link in a new tab
    webbrowser.open(pathName +"/testCases/TestReport.html",new=new)
    print(pathName + "/TestReport.html\n")

main()
