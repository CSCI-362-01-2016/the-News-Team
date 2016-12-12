# Youtube-dl Testing Framework.

Youtube-dl is an open source software that allows users to download online videos via a Linux terminal command.

##Running The test case framework:
In the main directory, look for the file "topLevelScript.py"

This file can be run from the terminal by typing "python3 topLevelScript.py"

topLevelScript.py contains the testing framework, and reads test cases from the testCases folder.
The framework reads these test cases, which contain a method and parameters to be tested, and then runs each method to verify its correctness.  After all tests are run, the results of the tests are outputted to an HTML table which is loaded in the user's browser.
