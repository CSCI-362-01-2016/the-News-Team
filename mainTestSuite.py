#!/usr/bin/env python
from __future__ import unicode_literals


import os
import sys
import webbrowser
from string import Template
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_dl.aes import aes_decrypt, aes_encrypt, aes_cbc_decrypt, aes_decrypt_text
from youtube_dl.utils import bytes_to_intlist, intlist_to_bytes
import base64
from test.helper import try_rm
from youtube_dl import YoutubeDL
import copy

from test.helper import FakeYDL, assertRegexpMatches
from youtube_dl import YoutubeDL
from youtube_dl.compat import compat_str, compat_urllib_error
from youtube_dl.extractor import YoutubeIE
from youtube_dl.extractor.common import InfoExtractor
from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl.utils import ExtractorError, match_filter_func

from test.helper import FakeYDL, md5


from youtube_dl.extractor import (
    YoutubeIE,
    DailymotionIE,
    TEDIE,
    VimeoIE,
    WallaIE,
    CeskaTelevizeIE,
    LyndaIE,
    NPOIE,
    ComedyCentralIE,
    NRKTVIE,
    RaiTVIE,
    VikiIE,
    ThePlatformIE,
    ThePlatformFeedIE,
    RTVEALaCartaIE,
    FunnyOrDieIE,
    DemocracynowIE,
)

htmlString = ""
testID = 0


os.chdir("..") #nove back one folder
pathName = str(os.path.dirname(os.path.abspath(__file__)))

def main1():
    parseTextFile()
    formatList =["Example Case","Example requirement","example component","example method","example inputs","example expected outcome(s)","example actual outcome","example PASS/FAIL"," example Test case","requirement","example component","example method","example inputs","example expected outcome(s)","example actual outcome"," example PASS/FAIL"]
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
    new = 2 # Code used to open html link in a new tab
    webbrowser.open(pathName +"/testCases/TestReport.html",new=new)
    print(pathName + "/TestReport.html\n")











#Test case running methods
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






class BaseTestSubtitles(unittest.TestCase):
    url = None
    IE = None

    def setUp(self):
        self.DL = FakeYDL()
        self.ie = self.IE()
        self.DL.add_info_extractor(self.ie)

    def getInfoDict(self):
        info_dict = self.DL.extract_info(self.url, download=False)
        return info_dict

    def getSubtitles(self):
        info_dict = self.getInfoDict()
        subtitles = info_dict['requested_subtitles']
        if not subtitles:
            return subtitles
        for sub_info in subtitles.values():
            if sub_info.get('data') is None:
                uf = self.DL.urlopen(sub_info['url'])
                sub_info['data'] = uf.read().decode('utf-8')
        return dict((l, sub_info['data']) for l, sub_info in subtitles.items())



#This class's methods test if a video has or does not have subtitles.
class TestYoutubeSubtitles(BaseTestSubtitles):
    url = 'QRS8MkLhQmM'
    IE = YoutubeIE

   
    def test_youtube_subtitles_ttml_format(self):
        self.DL.params['writesubtitles'] = True
        self.DL.params['subtitlesformat'] = 'ttml'
        subtitles = self.getSubtitles()
        self.assertEqual(md5(subtitles['en']), 'e306f8c42842f723447d9f63ad65df54')

    def test_youtube_automatic_captions(self):
        self.url = '8YoUxe5ncPo'
        self.DL.params['writeautomaticsub'] = True
        self.DL.params['subtitleslangs'] = ['it']
        subtitles = self.getSubtitles()
        self.assertTrue(subtitles['it'] is not None)

    def test_youtube_translated_subtitles(self):
        # This video has a subtitles track, which can be translated
        self.url = 'Ky9eprVWzlI'
        self.DL.params['writeautomaticsub'] = True
        self.DL.params['subtitleslangs'] = ['it']
        subtitles = self.getSubtitles()
        self.assertTrue(subtitles['it'] is not None)

    def test_youtube_nosubtitles(self):
        self.DL.expect_warning('video doesn\'t have subtitles')
        self.url = 'n5BB19UTcdA'
        self.DL.params['writesubtitles'] = True
        self.DL.params['allsubtitles'] = True
        subtitles = self.getSubtitles()
        self.assertFalse(subtitles)











class TestSuite(unittest.TestCase):

    #Some helper definitions


    #AES = advanced encryption standard
    #There is a flag in the Youtube downloader that lets the user also download
    #a description for the video.  The user has a choice to have that
    #description be encrypted with this encoding:
    def setUp(self):
        self.key = self.iv = [0x20, 0x15] + 14 * [0]
        #print(self.key)

    def test_encrypt(self):
        test5params = ["Hello world"]
        test6params = ["test Encryption message"]
        testparams = [test5params,test6params]
        for i in range(len(testparams)):
            print("Testing encrytption test case")
            msg = testparams[i]
            key = list(range(len(msg)))

            encryptedList = []
            for j in range(len(msg[0])):
                encryptedList.append(aes_encrypt(bytes_to_intlist(msg[0][j]), key))
            print("Encrypted:")
            print(encryptedList)
            decryptedList = ""
            for j in range(len(encryptedList)):
                decryptedList += intlist_to_bytes(aes_decrypt(encryptedList[j], key))
            print("Decrypted: ",decryptedList)

            global htmlString
            global testID
            htmlString += str(testID) + ",Test Description Encryption," + str(testparams[i]) +",True"
            testID += 1
            self.assertTrue(msg,decryptedList)

        
    #This method returns True to the video is restricted based on the user's age.
    def assert_restricted(self, url, filename, age, old_age=None):
        self.assertTrue(isRestricted(url, filename, old_age))
        self.assertFalse(isRestricted(url, filename, age))
        return "\nSuccess! Video downloaded\n"

    #This method makes sure that the minimum age is 0, which means no restriction.
    def assert_not_restricted(self, url, filename, age, old_age=None):
        self.assertTrue(isRestricted(url, filename, old_age))
        return "\nSuccess! Video downloaded\n"







    #==========================================================================
    #
    #These are the methods that actually run the tests.  The params arrays
    #Contain data that is to be read from the files.  Not sure how you do it
    #currently.
    #
    #==========================================================================
    def testCaseRestricted(self):
        test1params = ['07FYdnEawAQ', '07FYdnEawAQ.mp4', 10, 18]
        test2params = ['http://www.youporn.com/watch/505835/sex-ed-is-it-safe-to-masturbate-daily/',
            '505835.mp4', 10, 25]
        testparams = [test1params, test2params]
        for i in range(len(testparams)):
            print(self.assert_restricted(testparams[i][0],testparams[i][1],testparams[i][2],old_age=testparams[i][3]))

    def testCaseNotRestricted(self):
        test3params = ['07FYdnEawAQ', '07FYdnEawAQ.mp4', 28, 18]
        test4params = ['wduZHtRbSkY', 'wduZHtRbSkY.mp4', 10, 0]
        testparams = [test3params, test4params]


        for i in range(len(testparams)):
            print(self.assert_not_restricted(testparams[i][0],testparams[i][1],testparams[i][2],old_age=testparams[i][3]))




if __name__ == '__main__':
    unittest.main()
    print("PRINTING HTML=====================================")
    print(htmlString)


















main1()
