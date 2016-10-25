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

from test.helper import try_rm


from youtube_dl import YoutubeDL


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
        print("Test 1:")
        print("Video: 'Justin Timberlake - Tunnel Vision (Explicit)'")
        print("Subject age: 10")
        print("-------------------------------------------------")
        print(self.assert_restricted('07FYdnEawAQ', '07FYdnEawAQ.mp4', 10, old_age=18))

    #Second test- Verify video not restricted for adult user
    def test_youtube_normal1(self):
        print('\n')
        print("Test 2: Verify video is not restricted")
        print("Video: 'Justin Timberlake - Tunnel Vision (Explicit)'")
        print("Subject age: 28")
        print("-------------------------------------------------")
        print(self.assert_not_restricted('07FYdnEawAQ', '07FYdnEawAQ.mp4', 28, old_age=18))
    
    #Third test- Verify video not restricted
    def test_youtube_normal2(self):
        print('\n')
        print("Test 3: Verify video is not restricted")
        print("Video: '$4 Burger Vs. $777 Burger'")
        print("Subject age: 10")
        print("-------------------------------------------------")
        print(self.assert_not_restricted('wduZHtRbSkY', 'wduZHtRbSkY.mp4', 10))

        
    #Fourth test- Verify video is restricted
    def test_youporn(self):
        print('\n')
        print("Test 4: Verify video is restricted")
        print("Subject age: 15")
        print("-------------------------------------------------")
        print(self.assert_restricted(
            'http://www.youporn.com/watch/505835/sex-ed-is-it-safe-to-masturbate-daily/',
            '505835.mp4', 10, old_age=25))
   


if __name__ == '__main__':
    unittest.main()
