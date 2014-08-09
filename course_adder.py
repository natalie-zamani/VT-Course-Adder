#!/usr/bin/python

import mechanize, base64
from bs4 import BeautifulSoup
from time import sleep

def login(username, password, myBrowser):
	myBrowser.set_handle_robots(False)

	myBrowser.open("https://banweb.banner.vt.edu/ssb/prod/twbkwbis.P_WWWLogin")

	myBrowser.follow_link(text="Login to HokieSpa >>>")

	myBrowser.select_form(nr = 0)

	myBrowser["username"] = username

	myBrowser["password"] = password

	# And we're in!
	myBrowser.submit()

	myBrowser.follow_link(text="Hokie Spa")

	myBrowser.follow_link(text="Registration and Schedule")

	myBrowser.follow_link(text="Drop/Add", nr=0)


	'''
	------ Code below was used to find forms, links, etc ------
	print myBrowser.response().geturl()

	#print

	#print myBrowser.response().get_data()
	for link in myBrowser.links():
		print link.url

	for form in myBrowser.forms():
		for control in form.controls:
			print control
	'''

def add_course(myBrowser, crn):
	myBrowser.select_form(nr = 1)
	crnControl = myBrowser.find_control(id = "crn_id1")
	crnControl.readonly = False
	crnControl._value = crn
	response = crn.submit()
	responseText = response.get_data()

	if "Registration Errors" in responseText:
		# Unsuccessfully added.
		return False
	else:
		# Successfully added.
		return True

def filter_invalid_crns(classes):
	# Removes any elements from the list if the length is not 5.
	classes[:] = [crn for crn in classes if len(str(crn)) == 5]

def main():
	myBrowser = mechanize.Browser()
	username = raw_input("Enter your username: ")
	password = raw_input("Enter your password: ")
	
	classesToAdd = raw_input("Enter CRN's that you wish to add separated by spaces: ")
	classesToAdd = map(int, classesToAdd.split())

	# CRN's must 5 numbers long. Get rid of any that are not.
	filter_invalid_crns(classesToAdd)

	login(username, password, myBrowser)
	add_course(myBrowser)

	# Runs the script until all classes are successfully added.
	while len(classesToAdd) > 0:
		classesToAdd[:] = [crn for crn in classesToAdd if !add_course(myBrowser, crn)]
		# Idles for 30 seconds before attempting again.
		sleep(30)

if __name__ == "__main__": main()