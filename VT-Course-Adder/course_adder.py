#!/usr/bin/python

import mechanize, base64
from bs4 import BeautifulSoup

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

def add_course(myBrowser):
	pass

def main():
	myBrowser = mechanize.Browser()
	username = raw_input("Enter your username: ")
	password = raw_input("Enter your password: ")
	login(username, password, myBrowser)
	add_course(myBrowser)

if __name__ == "__main__": main()