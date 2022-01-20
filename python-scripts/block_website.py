# Run this script as root

import time
from datetime import datetime as dt

# change hosts path according to your OS
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# localhost's IP
redirect = "127.0.0.1"

# prompt user with input
siteNum = int(input("How many site(s) do you want to block:"))

for i in range(1, siteNum+1):
    website_list = []
    website = input("Enter the site url to block:")
    website_list.append(website)


# Timing
startTime = int(input("Enter the starting time to block the site (in 24hr format)"))
endTime = int(input("Enter the end time to block the site (in 24hr format)"))

# Initiate an infinte loop to check for the time
while True:
    # In working hours
    if dt(dt.now().year, dt.now().month, dt.now().day, startTime) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, endTime):
        print("Working hour")
        # Open host file
        with open(hosts_path,'r+') as file:
            #Read the file content
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    #Write the redirect ip + space + website url
                    file.write(redirect+" "+website+"\n")
    # In free hours
    else:
        print("Fun hour")
        #Remove the blocked site
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(600)



