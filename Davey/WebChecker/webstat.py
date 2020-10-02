##### This should run in Linux and Windows.
##### Using the "command prompt" or "bash" 

##### Usage : 
#####              python  webstat.py
#####
##### for python 3,
#####              python3  webstat.py
#####
#############################################
#####  GNU License version 2  is always implied in using this
#####  script.
##### The author expects you to know that LICENSE and DISCLAIMER.
#############################################




#####modules required in accessing web servers using http
#####and or https as well as for system console.
import os
import platform
import requests as req

#####best to display a clean output depending
#####on what type of OS this script is running.
#####Linux and Windows only. Apologies to
#####Mac users.   :-)

ourOS = platform.system()

if ourOS == "Linux":
	
	os.system('clear')
	
else:
	os.system('cls')
	
	
print(" \n")


#####querying of GSMS web server starts here
print("-------------------- GSMS ------------------------\n")


####Use catch definition in python to trap any unexpected errors.
####Prevents display of full stack trace back using the generic 
####standard Exception class. Python 2 and Python 3 have
####different error hierarchy, so We are using this class
####so that it will work in both Python versions.
try:
	resp = req.get("http://180.232.111.41")
	resp2 = req.get("http://122.53.177.137")
	if resp.status_code == 200:
		print ("GSMS log-in page using ISP1 is operational.")
	else:
		print ("GSMS Web server or ISP1 is down.")
	
	if resp2.status_code == 200:
		print ("GSMS log-in page using ISP2 is operational.")
	else:
		print ("GSMS Web server or ISP2 is down.")
	
except Exception:
	print("Unable to access GSMS assigned IPs.")
	
print("--------------------------------------------------\n")	



#####querying of AISS web server starts here
print("-------------------- AISS ------------------------\n")

try:
	resp = req.get("http://180.232.111.40")
	resp2 = req.get("http://122.53.177.136")
	if resp.status_code == 200:
		print ("AISS  using ISP1 is operational.")
	else:
		print ("ISP1 is down.")
	
	if resp2.status_code == 200:
		print ("AISS  using ISP2 is operational.")
	else:
		print ("ISP2 is down.")

except Exception:
	print("Unable to access AISS assigned IPs.")

print(" \n")


try:
	####The IBS is using redirect from static DNS suppllied by 
	####CAAP. So, we should query it separately from IPs supplied
	####by our two ISPs
	resp = req.get("https://aiss.caap.gov.ph/fwf-caap/")


	if resp.status_code == 200:
		print ("AISS Web portal or IBS is operational.")
	else:
		print ("AISS Web server is down.")

	print("--------------------------------------------------\n")	

except Exception:
	print("Error occurred while re-directing to  AISS web server.")
	print("This could be an illegal entry in DNS list.\n")
	
