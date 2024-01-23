# 1. Отримайте поточний статус війни як англійською, так і українською мовою.

# import requests

# r1 = requests.get("https://russianwarship.rip/api/v2/war-info/status")
# print (r1.status_code)
# print (r1.headers)
# my_json1 = r1.json()
with open ("my_file_json1.json", "w") as my_file:
    json.dump(my_json1,my_file)



# 2. Отримайте останню статистику по війні
import requests

r2 = requests.get("https://russianwarship.rip/api/v2/statistics/latest")
print (r2.status_code)
print (r2.headers)
my_json2 = r2.json()
with open ("my_file_json2.json", "w") as my_file:
    json.dump(my_json2,my_file)

# 3. Отримайте статистику за 2 різні дні (виберіть дату самостійно).
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