import requests
url = 'http://104.129.186.123:5000/iptest'
headers = {'User-Agent':'kid_mozilla'}
r = requests.get(url,params=0,headers=headers)
r.text
