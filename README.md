# CSVprocessing
Code to convert CSV file into a list of dictionaries or dictionary of dictionaries. Code to write a list of dictionaries into a CSV file. CSV files are attached so you can test code.
# Installation
Install python 3. 
Preffered Method: 
python3 with anaconda(https://www.anaconda.com/download/#macos)
#
OS X: 
http://docs.python-guide.org/en/latest/starting/install3/osx/
#
Windows: 
http://docs.python-guide.org/en/latest/starting/install3/win/
#
Linux: 
http://docs.python-guide.org/en/latest/starting/install3/linux/
# Running Code
Preffered Method: open Spyder from anaconda. Spyder is open source IDE that automatically comes with several scripting libraries.
#
OS X: 
1. Create a folder to run code in this repo. Download the code and csv files and move it to this folder.
2. Open Terminal.
3. cd to the folder
4. Type "python ./csvread.py" to run this program. 
NOTE: If you have python 2 and python 3 installed run "python3 csvread.py"
#
Windows:
1. Create a folder to run code in this repo. Download the code and csv files and move it to this folder.
2. Open Command Prompt.
3. cd \ to the folder
4. Type "csvread.py" to run this program. 
NOTE: If it didn't work, make sure your PATH contains the python directory.
#
Linux: 
1. Create a folder to run code in this repo. Download the code and csv files and move it to this folder.
2. Open up the terminal program. In KDE, open the main menu and select "Run Command..." to open Konsole. In GNOME, open the main menu, open the Applications folder, open the Accessories folder, and select Terminal.
3. cd ~/ to the folder
4. Type "chmod a+x csvread.py" to tell Linux that it is an executable program.
5. Type "./csvread.py" to run this program. 
# Testing
Functions: test_csv_fieldnames, test_list_dict, test_nested_dict, and test_write test all the other functions in this program to see if they do what they say they do. Note that instead of a dictionary you will get a OrderedDict object as output this is inevitable but in essence an OrderedDict object is the same as a dictionary for this case. To get more informaiton on what an OrderedDict object is refer to 
this link, https://docs.python.org/3/library/collections.html#collections.OrderedDict. If you look at csvread.py you will notice that the test functions use table1.csv to test the code you can use any of the 7 files provided so as long as you change the separator, quote and keyfields.


