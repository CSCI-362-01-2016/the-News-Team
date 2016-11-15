#!/usr/bin/env python
import os
import webbrowser
from string import Template


os.chdir("..") #nove back one folder
pathName = str(os.path.dirname(os.path.abspath(__file__)))

def main():

    formatList =["Example Case","Example requirement","example component","example method","example inputs","example expected outcome(s)","example actual outcome","example PASS/FAIL"," example Test case","requirement","example component","example method","example inputs","example expected outcome(s)","example actual outcome"," example PASS/FAIL"]
    textToHtml(fakeexecuteTestCases())
    # executeTestCase(parseTextFile())
    loadOutputInBrowser()

def parseTextFile():
    #number of text files to parse
    txtFileCount = 0
    os.chdir("testCases") #move into the test cases folder

    #gathering count of test case files
    dataList = []
    for file in os.listdir(os.getcwd()):
        # dataList in the form of
        # [0] Test number
        # [1] Requirement being tested
        # [2] Component being tested
        # [3] Method being tested
        # [4] Test input
        # [5] Expected Outcomes


        if file.endswith(".txt"):
            txtFileCount += 1

            inputFile = open(file, "r")
            for line in inputFile:
                dataList.append(line)

            inputFile.close()
    return dataList


def fakeexecuteTestCases():
    tempList = parseTextFile()
    returnList = tempList.copy()
    for i in range(tempList.__len__()-1,0,-1):

        if i % 7 == 0:
            returnList.insert(i,"pass")
    print(returnList)
    return returnList

def executeTestCase(listTests):
    print(listTests)
    os.chdir("..")
    os.chdir("project")
    os.chdir("youtube_dl")
    print(os.getcwd())
    numberOfTests = listTests.__len__() // 6
    print(numberOfTests)
    for i in range(0,numberOfTests-1):
        for z in range(1,9):
            temp = listTests[(i*6)+z]
            if(z == 2):
                temp = temp.split("/")
                print(temp[1])
                print(os.getcwd())
                temp[1]= temp[1].strip()
                print(temp[1])


    os.chdir("..")
    return;

def writeOutputToHtml():
    return;
def textToHtml(listOutput):
    os.chdir("..")
    os.chdir("scripts")
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
    webbrowser.open(pathName +"/TestReport.html",new=new)
    print(pathName + "/TestReport.html\n")

main()
