import time
from datetime import datetime as dt

"""
Stop_Discord: Block_Websites.py
Stops user interaction during the period of 0600 to 1700 (6AM-5PM) to websites specified in website_list
to encourage productivity.

"""


hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.discord.com", "discord.com", "www.reddit.com", "reddit.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 6) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Focus on work.")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Time to relax.")
    time.sleep(10)
