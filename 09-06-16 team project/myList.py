import os
import webbrowser
from string import Template

pathName = str(os.path.dirname(os.path.abspath(__file__)))

def convert_to_text():
    #This takes the current directory from where the script is being run and stores it
    #in a variable for later use
    print("The current path the script is running on is " + pathName + "\n")
    #This stores the contents of the directory where the script is running as a list
    contentsList = os.listdir(pathName)

    #Loops through the contents list and prints contents
    print("The current items in the directory where the script is being run are: ")
    #Opening the text file, will be created if it does not already exist
    textOuput = open("TextForHtml.txt", "w")
    i = -1
    for item in contentsList:
        i += 1
        print("Item #" + str(i + 1) + ": " + contentsList[i])
        textOuput.write(contentsList[i] + "\n")
    textOuput.close()

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

def openInBrower():
    new = 2  # Code used to open html link in a new tab
    webbrowser.open(pathName +"/Output.html",new=new)
    print(pathName + "Output.html\n")

def main():
    convert_to_text()
    textToHtml()
    openInBrower()

main()