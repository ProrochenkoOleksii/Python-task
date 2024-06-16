#1. robots.txt
# Download and save robots.txt file from websites like Wikipedia, Twitter, etc.

import requests

r = requests.get('https://www.wikipedia.org/')
r_s=str(r.status_code)
r_h=r.headers
r_t=r.text


with open ("robots.txt", "w") as my_file:
    my_file.write("Status:" + r_s + "\n")
    my_file.write("Header:" + r_h + "\n")
    my_file.write("Text:" + r_t + "\n")



# 2. Check out the fresh API https://russianwarship.rip/api-documentation/v2.
# (general site - https://russianwarship.rip/). Try to work with 2-3 endpoints (URLs)
# to choose and download the received data into a JSON file


import requests
import json

r1 = requests.get("https://russianwarship.rip/api/v2/terms/en")
r_s1 = str(r1.status_code)
r_h1 = r1.headers
# r_t1 = r1.text
r_j1 = r1.json()
with open ("file_url1.json", "w") as my_file:
    json.dump(r_j1,my_file)
    

r2 = requests.get("https://russianwarship.rip/api/v2/war-info/status")
r_s2 = str(r2.status_code)
r_h2 = r2.headers
# r_t2 = r2.text
r_j2 = r2.json()
with open ("file_url2.json", "w") as my_file2:
    json.dump(r_j2,my_file2)

