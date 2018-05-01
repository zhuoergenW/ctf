import requests
url = 'http://104.129.186.123:5000/iptest'
myip = '4.4.4.4'
headers = {'X-Forward-For': myip}
r = requests.get(url,params=0,headers=headers)
r.text
