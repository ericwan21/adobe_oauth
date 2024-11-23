import requests

url = "https://ims-na1.adobelogin.com/ims/token/v3"

API_KEY = "REPLACE_ME"
CLIENT_SECRET = "REPLACE_ME"
SCOPES = ["openid", "AdobeID", "read_organizations", "additional_info.projectedProductContext", "additional_info.job_function"]

scopes_string = ",".join(SCOPES)
payload = f'client_id={API_KEY}&client_secret={CLIENT_SECRET}&grant_type=client_credentials&scope={scopes_string}'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)