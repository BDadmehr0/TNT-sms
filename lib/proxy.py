import requests
import os
import random
import signal

data = {
    'UrlBox': 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all',
    'AgentList': 'Internet+Explorer',
    'VersionsList': 'HTTP%2F1.1',
    'MethodList': 'GET',
}

random_number = random.randint(366, 2057)
# end = 2057
# start = 366
url = 'https://api.ipify.org?format=json'

response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', json=data)
proxies = response.text.split('\n')

proxych = proxies[random_number].replace(' ', '').replace('\t', '').replace('\n', '')

proxy = {
    'https': f'https://{proxych}'
}

response = requests.get(url, proxies=proxy)
print(response.text)

