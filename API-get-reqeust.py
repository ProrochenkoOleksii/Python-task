# 1. Get the current war status in both English and Ukrainian.
# import requests

# r1 = requests.get("https://russianwarship.rip/api/v2/war-info/status")
# print (r1.status_code)
# print (r1.headers)
# my_json1 = r1.json()
with open ("my_file_json1.json", "w") as my_file:
    json.dump(my_json1,my_file)


# 2. Get the latest war statistics
import requests

r2 = requests.get("https://russianwarship.rip/api/v2/statistics/latest")
print (r2.status_code)
print (r2.headers)
my_json2 = r2.json()
with open ("my_file_json2.json", "w") as my_file:
    json.dump(my_json2,my_file)

# 3. Get statistics for 2 different days (choose the date yourself).
# import requests

# r3 = requests.get("https://russianwarship.rip/api/v2/statistics/2023-09-30")
# print (r3.status_code)
# print (r3.headers)
# my_json3 = r3.json()
with open ("my_file_json3.json", "w") as my_file:
    json.dump(my_json3,my_file)


# r4 = requests.get("https://russianwarship.rip/api/v2/statistics/2024-01-13")
# print (r4.status_code)
# print (r4.headers)
# my_json4 = r4.json()
with open ("my_file_json4.json", "w") as my_file:
    json.dump(my_json4,my_file)
