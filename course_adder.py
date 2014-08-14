#!/usr/bin/python

import mechanize, base64
from bs4 import BeautifulSoup
from time import sleep

def login(username, password, myBrowser):
	try:
		myBrowser.open("https://banweb.banner.vt.edu/ssb/prod/twbkwbis.P_WWWLogin")

		myBrowser.follow_link(text="Login to HokieSpa >>>")

		myBrowser.select_form(nr = 0)

		myBrowser["username"] = username

		myBrowser["password"] = password

		myBrowser.submit()

		myBrowser.follow_link(text="Hokie Spa")

		myBrowser.follow_link(text="Registration and Schedule")

		myBrowser.follow_link(text="Drop/Add", nr=0)
	except:
		print "Error logging in, attempting again..."
		login(username, password, myBrowser)



def add_course(myBrowser, crn):
	myBrowser.select_form(nr = 1)
	crnControl = myBrowser.find_control(id = "crn_id1")
	crnControl.readonly = False
	crnControl._value = crn
	response = myBrowser.submit()
	responseText = response.get_data()

	if "Registration Errors" in responseText:
		# Unsuccessfully added.
		print "CRN:", crn, "unsuccessfully added. Trying again in 30 seconds."
		return False
	else:
		# Successfully added.
		print "CRN:", crn, "successfully added. Removing from the list."
		return True

def filter_invalid_crns(classes):
	# Removes any elements from the list if the length is not 5.
	classes[:] = [crn for crn in classes if len(str(crn)) == 5]

def main():
	myBrowser = mechanize.Browser()
	myBrowser.set_handle_robots(False)
	username = raw_input("Enter your username: ")
	password = raw_input("Enter your password: ")
	
	classesToAdd = raw_input("Enter CRN's that you wish to add separated by spaces: ")
	classesToAdd = map(int, classesToAdd.split())

	# CRN's must 5 numbers long. Get rid of any that are not.
	filter_invalid_crns(classesToAdd)

	login(username, password, myBrowser)

	print "Successfully logged in. Beginning course add attempts."

	# Runs the script until all classes are successfully added.
	while len(classesToAdd) > 0:
		classesToAdd[:] = [crn for crn in classesToAdd if not add_course(myBrowser, crn)]
		# Idles for 30 seconds before attempting again.
		sleep(30)

	print "All courses added."

if __name__ == "__main__": main()