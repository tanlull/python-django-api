import requests
 
url = "https://api.aiforthai.in.th/ssense"
 
text = 'ลงุตู่น่ารักจังเลย'
 
params = {'text':text}
 
headers = {
    'Apikey': "buZ5tUWbWGNK35jLesFoFwkZ3Cn5gvbB"
    }
 
response = requests.get(url, headers=headers, params=params)
 
print(response.json())