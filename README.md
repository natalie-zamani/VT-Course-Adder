What this script does
==============
This script uses the Python mechanize library to attempt to add courses for you based on the CRNs you provide. Attempts to add courses every 30 seconds until all CRNs provided have been successfully added to your schedule.


How to use this script
===============
For these instructions, I will assume that you have Python 2.7.x, pip, and Git installed. If you do not, see the following links: <br />
1. [Download the latest version of Python 2](https://www.python.org/downloads/) <br />
2. [Download pip](https://pip.pypa.io/en/latest/installing.html) <br />
3. (Optional) [Download Git](http://git-scm.com/downloads) <br />

##OS X/Linux:
1. Open the Terminal/Command Line application.
2. Navigate to the directory you would like to save this script. ([See this link for reference.](http://guides.macrumors.com/Terminal))
3. Either download and unzip the script, or (if you have Git installed) type: `git clone git@github.com:mzamani1/VT-Course-Adder.git`
4. Type `cd VT-Course-Adder/` to change into the directory with the script.
5. Type `pip install -r requirements.txt` to install the script dependencies.
6. Type `chmod 755 course_adder.py` to allow the script to be executed.
7. Type `./course_adder.py` to run the script.

##Windows
1. Open up Command Prompt.
2. Change into the directory you would like to save this script. ([See this link for reference.] (http://www.wikihow.com/Change-Directories-in-Command-Prompt))
3. Either download and unzip the script, or (if you have Git installed) type: `git clone git@github.com:mzamani1/VT-Course-Adder.git`
4. Type `cd VT-Course-Adder`
5. Type `pip install -r requirements.txt` to install the script dependencies.
6. Type `python course_adder.py` to run the script.

##Notes
1. Depending on the term and year of the semester that you are attempting to add courses for, modify the "termYear" variable located at the top of the program. For instance, for Spring 2015 a vaue of "201501" should be entered.
2. The variable "numberOfDropAddLinkToFollow" must be modified depending on which link on the Registration and Schedule site corresponds to the semester you are attempting to run this script for. Note that this value must be 0-indexed (i.e., start counting from 0 instead of 1).
