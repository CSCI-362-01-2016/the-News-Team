This script reads the files in this directory and writes the files to an html file and displays it
myList.py file is the source code
myList.sh is a driver for myList.py that enforces a python 3 execution.

1)If you want to be able to double click and execute myList.sh follow these steps:

Hit Alt+F2, type dconf-editor and hit Enter.

If you get an error message saying that dconf-editor isn't installed, install dconf-editor with
sudo apt install dconf-editor
run dconf-editor

In dconfg-editor goto: org ➤ gnome ➤ nautilus ➤ preferences
Click on executable-text-activation and from drop down menu select:
launch: to launch scripts as programs.

2)If you wish to run myList.sh from the terminal....
open the terminal
navigate to the directory that myList.sh is contained in
type "sh myList.sh" without the quotes
and press enter
