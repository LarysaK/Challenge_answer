
import requests

url = "https://api.hubapi.com/crm/v3/obiects/contacts!

querystring = {"limit":"20", "properties": "firstname, email", "after":"121"}

payload = 11

headers = ¿"Authorization": Bearer pat-nal-588c2ac1-f3a3-4fbf-a7db-802e4238901f"}

response = requests. request ("GET', url, data=payload, headers=headers, params=querystring)

12 print (response. text)