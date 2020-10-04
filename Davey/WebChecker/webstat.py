import sys, time, threading
import os
import platform
import requests as req


# Our spinner function, not necessarily
# required but for classiness-sake only
def spin_cursor():
    while True:
        for cursor in '|/-\\':
            sys.stdout.write(cursor)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
            if done:
                return

# start the spinner in a separate thread
done = False
spin_thread = threading.Thread(target=spin_cursor)


# do some more work in the main thread
ourOS = platform.system()

if ourOS == "Linux":
	
	os.system('clear')
	
else:
	os.system('cls')
	
	
print(" \n")


#####querying of GSMS web server starts here
print("-------------------- GSMS ------------------------\n")

spin_thread.start()
####Use catch definition in python to trap any unexpected errors.
####Prevents display of full stack trace back using the generic 
####standard Exception class. Python 2 and Python 3 have
####different error hierarchy, so We are using this class
####so that it will work in both Python versions.
try:
	resp = req.get("http://180.232.111.41")
	resp2 = req.get("http://122.53.177.137")
	done = True
	spin_thread.join()
	if resp.status_code == 200:
		print ("GSMS log-in page using ISP1 is operational.")
	else:
		print ("GSMS Web server or ISP1 is down.")
	
	if resp2.status_code == 200:
		print ("GSMS log-in page using ISP2 is operational.")
	else:
		print ("GSMS Web server or ISP2 is down.")
	
except Exception:
	done = True
	spin_thread.join()
	print("Unable to access GSMS assigned IPs.")
	
print("--------------------------------------------------\n")	



#####querying of AISS web server starts here
print("-------------------- AISS ------------------------\n")
done = False
spin_thread = threading.Thread(target=spin_cursor)
spin_thread.start()
try:
	resp = req.get("http://180.232.111.40")
	resp2 = req.get("http://122.53.177.136")
	done = True
	spin_thread.join()
	if resp.status_code == 200:
		print ("AISS  using ISP1 is operational.")
	else:
		print ("ISP1 is down.")
	
	if resp2.status_code == 200:
		print ("AISS  using ISP2 is operational.")
	else:
		print ("ISP2 is down.")

except Exception:
	done = True
	spin_thread.join()
	print("Unable to access AISS assigned IPs.")

print(" \n")


done = False
spin_thread = threading.Thread(target=spin_cursor)
spin_thread.start()
try:
	####The IBS is using redirect from static DNS suppllied by 
	####CAAP. So, we should query it separately from IPs supplied
	####by our two ISPs
	resp = req.get("https://aiss.caap.gov.ph/fwf-caap/")
	done = True
	spin_thread.join()
	


	if resp.status_code == 200:
		print ("AISS Web portal or IBS is operational.")
	else:
		print ("AISS Web server is down.")

	print("--------------------------------------------------\n")	

except Exception:
	done = True
	spin_thread.join()
	print("Error while re-directing to  AISS web server.")
	print("This could be an illegal entry in DNS list.\n")



print("all done.\n")