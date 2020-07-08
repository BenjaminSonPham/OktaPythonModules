import requests,sys


payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'SSWS 00HoWOPgJfloCvXdoJeAi2qZoEIvmwMkjF2ZhI3IjP',
}

list_groups_url = "https://ben-tevora.oktapreview.com/api/v1/groups"
groups_request = requests.request("GET", list_groups_url, headers=headers, data = payload)
groups_list = groups_request.json()

print(groups_list)
print(len(groups_list))

ghost_groups = []

for group in groups_list:
  id = group['id']
  group_member_url = "https://ben-tevora.oktapreview.com/api/v1/groups/"+ id + "/users"
  group_member_request = requests.request("GET",group_member_url, headers=headers, data=payload)

  group_apps_url = "https://ben-tevora.oktapreview.com/api/v1/groups/"+ id + "/apps"
  group_apps_request = requests.request("GET",group_member_url, headers=headers, data=payload)

  group_members = group_member_request.json()
  group_apps = group_apps_request.json()

  if len(group_members) == 0 and len(group_apps) == 0:
    ghost_groups.append(group)

print(len(groups_list))
print(len(ghost_groups))
