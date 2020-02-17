import sys,csv,json,requests,mimetypes
import multiprocessing

okta_tenant = "https://tevora.oktapreview.com"
api_key = "00E8wu3JE19SDwDqZvutlc5zB8EJULIe-MILeDTgyz"
payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'SSWS '+ api_key 
}

def is_user_MFA_enrolled(userID):
    api_endpoint = "/api/v1/users/" + userID + "/factors/catalog"
    url = okta_tenant + api_endpoint 
    response = requests.request("GET", url, headers=headers, data = payload)

    user_mfa_list = response.json()
    if len(user_mfa_list) > 0:
        is_user_mfa_enrolled = False
        for mfa in user_mfa_list:
            if mfa['status'] == 'ACTIVE':
                is_user_mfa_enrolled = True
                print(
                    mfa['factorType'])

        return is_user_mfa_enrolled

    else:
        return False 

def process_user(url):
   return requests.request("GET", url, headers=headers, data = payload)


api_endpoint = "/api/v1/users?limit=200" 

while True:
    url = okta_tenant + api_endpoint
    if (url):
        break
    user_list_json = process_user(api_endpoint)
    api_endpoint = 





