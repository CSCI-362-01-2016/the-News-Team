#!/usr/bin/env python
from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest
#unittest is a normal Python class that supports testing a class.
#In this case, the class to be tested is the TestAgeRescriction class.
#The last two lines run all of the methods in the classes which contain the
#parameters of unittest and TestCase.

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_dl.aes import aes_decrypt, aes_encrypt, aes_cbc_decrypt, aes_decrypt_text
from youtube_dl.utils import bytes_to_intlist, intlist_to_bytes
import base64
from test.helper import try_rm


from youtube_dl import YoutubeDL


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
      <title>Test CAses</title>
    </head>
    <body>
        <h1>Test Cases:</h1>
      <p>$output</p>
    </body>
    </html>""")

    f=open('testfile', 'r')
    f2= f.read()
    f.close()
    
    files = f2;

    
    #for line in inf:
    #    files += line + "<br>"

    outf.write(template.substitute(output=files))
    inf.close()
    outf.close()

def openInBrower():
    new = 2  # Code used to open html link in a new tab
    webbrowser.open(pathName +"/Output.html",new=new)
    print(pathName + "Output.html\n")











def isRestricted(url, filename, age):
    """ Returns true if the file has been downloaded """

    params = {
        'age_limit': age,
        'skip_download': True,
        'writeinfojson': True,
        'outtmpl': '%(id)s.%(ext)s',
    }
    ydl = YoutubeDL(params)
    ydl.add_default_info_extractors()
    json_filename = os.path.splitext(filename)[0] + '.info.json'
    try_rm(json_filename)
    ydl.download([url])
    res = os.path.exists(json_filename)
    try_rm(json_filename)
    print "Download method: ",filename,res
    return res


class TestSuite(unittest.TestCase):

    #Some helper definitions


    #AES = advanced encryption standard
    #There is a flag in the Youtube downloader that lets the user also download
    #a description for the video.  The user has a choice to have that
    #description be encrypted with this encoding:
    def setUp(self):
        self.key = self.iv = [0x20, 0x15] + 14 * [0]
        #print(self.key)
        self.secret_msg = b'Secret message goes here'

    #Note, this function can only encrypt messages 16 characters at a time.
    def test_encrypt(self):
        msg = b'Hello world'
        key = list(range(len(msg)))
        print()
        print("Testing video description encrypting function")
        print("Original message:")
        print(msg)
        encrypted = aes_encrypt(bytes_to_intlist(msg), key)
        print("Encrypted:")
        print(encrypted)
        decrypted = intlist_to_bytes(aes_decrypt(encrypted, key))
        print("Decrypted:")
        print(decrypted)

        
    #This method returns True to the video is restricted based on the user's age.
    def assert_restricted(self, url, filename, age, old_age=None):
        self.assertTrue(isRestricted(url, filename, old_age))
        self.assertFalse(isRestricted(url, filename, age))
        return "\nSuccess! Video downloaded\n"

    #This method makes sure that the minimum age is 0, which means no restriction.
    def assert_not_restricted(self, url, filename, age, old_age=None):
        self.assertTrue(isRestricted(url, filename, old_age))
        return "\nSuccess! Video downloaded\n"



    #First test- Verify age restriction on a video with bad language.
    def test_youtube(self):
        print('\n')
        print("Test 1: Test video is restricted")
        print("Video: 'Justin Timberlake - Tunnel Vision (Explicit)'")
        print("Subject age: 10")
        print("-------------------------------------------------")
        print(self.assert_restricted('07FYdnEawAQ', '07FYdnEawAQ.mp4', 10, old_age=18))
        f=open('testfile', 'a')
        f.write("<br><h1>Test1 Verify video not restricted:</h1><br>Video: 'Justin Timberlake - Tunnel Vision (Explicit)'<br>Subject age: 10<br>"+self.assert_restricted('07FYdnEawAQ', '07FYdnEawAQ.mp4', 10, old_age=18))
        f.close()
        

    #Second test- Verify video not restricted for adult user
    def test_youtube_normal1(self):
        print('\n')
        print("Test 2: Verify video is not restricted")
        print("Video: 'Justin Timberlake - Tunnel Vision (Explicit)'")
        print("Subject age: 28")
        print("-------------------------------------------------")
        print(self.assert_not_restricted('07FYdnEawAQ', '07FYdnEawAQ.mp4', 28, old_age=18))
        f=open('testfile', 'a')
        f.write("<br><h1>Test2:  Verify video is not restricted</h1><br>Video: 'Justin Timberlake - Tunnel Vision (Explicit)'<br>Subject age: 28<br>"+self.assert_not_restricted('07FYdnEawAQ', '07FYdnEawAQ.mp4', 28, old_age=18))
        f.close()
    
    #Third test- Verify video not restricted
    def test_youtube_normal2(self):
        print('\n')
        print("Test 3: Verify video is not restricted")
        print("Video: '$4 Burger Vs. $777 Burger'")
        print("Subject age: 10")
        print("-------------------------------------------------")
        print(self.assert_not_restricted('wduZHtRbSkY', 'wduZHtRbSkY.mp4', 10))
        f=open('testfile', 'a')
        f.write("<br><h1>Test3: Verify video is not restricted</h1><br>Video: Video: '$4 Burger Vs. $777 Burger'<br>Subject age: 10<br>"+self.assert_not_restricted('wduZHtRbSkY', 'wduZHtRbSkY.mp4', 10))
        f.close()

        
    #Fourth test- Verify video is restricted
    def test_youporn(self):
        print('\n')
        print("Test 4: Verify video is restricted")
        print("Subject age: 15")
        print("-------------------------------------------------")
        print(self.assert_restricted(
            'http://www.youporn.com/watch/505835/sex-ed-is-it-safe-to-masturbate-daily/',
            '505835.mp4', 10, old_age=25))
        f=open('testfile', 'a')
        f.write("<br><h1>Test4: Verify video is restricted</h1><br>Subject age: 10<br>"+self.assert_restricted(
            'http://www.youporn.com/watch/505835/sex-ed-is-it-safe-to-masturbate-daily/',
            '505835.mp4', 10, old_age=25))
        f.close()


convert_to_text()
textToHtml()
openInBrower()

if __name__ == '__main__':
    unittest.main()
convert_to_text()
textToHtml()
openInBrower()
