#!/usr/bin/env python
import os
import webbrowser
from string import Template
import importlib
import sys

from project.youtube_dl import utils

sys.path.append(os.getcwd())
from scripts.youtube_dl.utils import formatSeconds

# nove back one folder
pathName = str(os.path.dirname(os.path.abspath(__file__)))


def main():
    formatList = ["Example Case", "Example requirement", "example component", "example method", "example inputs",
                  "example expected outcome(s)", "example actual outcome", "example PASS/FAIL", " example Test case",
                  "requirement", "example component", "example method", "example inputs", "example expected outcome(s)",
                  "example actual outcome", " example PASS/FAIL"]
    # formatSeconds(4543)
    outstr = executeTestCase(parseTextFile())
    textToHtml(outstr)
    # executeTestCase(parseTextFile())
    loadOutputInBrowser()


def parseTextFile():
    # number of text files to parse
    txtFileCount = 0
    os.chdir("testCases")  # move into the test cases folder

    # gathering count of test case files
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
                dataList.append(line.strip())

            inputFile.close()
    return dataList


def fakeexecuteTestCases():
    tempList = parseTextFile()
    returnList = tempList.copy()
    print(tempList.__len__())
    for i in range(tempList.__len__(), 0, -1):

        if (i) % 6 == 0:
            returnList.insert(i, "pass")
    print(returnList)
    return returnList


def executeTestCase(listTests):
    returnList = listTests.copy()
    os.chdir("..")
    os.chdir("project")
    numberOfTests = listTests.__len__() // 6
    index = 0
    for i in range(0, numberOfTests):
        for z in range(1, 7):

            if (z == 2):
                # print(index)
                temp = listTests[(i * 6) + z]
                # todo make an if statment making sure that the file is in the base youtube_dl folder
                os.chdir("youtube_dl")  # get into folder
                temp = temp.split("/")
                temp[1] = temp[1].strip()  # the name of the method to call
                paramaterList = listTests[index + 3].split(";")
                listTests[index + 2] = listTests[index + 2].strip()

                for z in range(0, paramaterList.__len__()):
                    paramaterList[z] = paramaterList[z].strip()  # paramater for method to be called
                # print(listTests[index+2])

                if (paramaterList[0].isdigit()):
                    paramaterList[0] = int(paramaterList[0])
                # todo dont hardcode default into untils here
                returnInput = str(getattr(utils, listTests[index + 2])(*paramaterList)).strip()
                os.chdir("..")  # gets our of folder
                returnList.insert(index + 5 + i * 2, returnInput == listTests[index + 4])
                returnList.insert(index + 5 + i * 2, returnInput)
            index += 1

    os.chdir("..")
    return returnList


def writeOutputToHtml():
    return


def textToHtml(listOutput):
    os.chdir("scripts")
    outf = open("TestReport.html", "w")
    template = Template("""<!doctype html>

    <html lang="en">
    <head>
      <meta charset="utf-8">

      <title>Test Report</title>
      <style>
        table {
            width:100%;
        }
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
        table tr:nth-child(even) {
            background-color: #eee;
        }
        table tr:nth-child(odd) {
            background-color:#FFF;
        }
        table th {
            background-color: black;
             color: white;
        }
       </style>

    </head>

    <body>
        <table style="width:100%;">
      $output
      </table>
    </body>
    </html>""")
    out = ""
    index = 0
    formatList = ["Test case", "Requirement", "Component", "Method", "Inputs", "Expected outcome(s)", "Actual outcome",
                  "PASS"]
    while index < len(listOutput) - 5:
        out += "<tr>"
        for i in range(0, 8):
            if (index < 8):
                out = out + "<th>" + formatList[i] + "</th>"
            else:
                if(str(listOutput[index-8]) == str(True)):
                    out = out + "<td style=\"background:green;\"><xmp>" + str(listOutput[index-8]) + "</xmp></td>"
                else:
                    out = out + "<td><xmp>" + str(listOutput[index-8]) + "</xmp></td>"
            index += 1
        out += "</tr>"

    outf.write(template.substitute(output=out))
    outf.close()


def loadOutputInBrowser():
    new = 2  # Code used to open html link in a new tab
    webbrowser.open(pathName + "/scripts/TestReport.html", new=new)
    print(pathName + "/TestReport.html\n")


main()
