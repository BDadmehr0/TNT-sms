import requests
import os

end = 2057
start = 366
url = 'https://api.ipify.org?format=json'


    
counter = 0 
data = {
    'UrlBox': 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all',
    'AgentList': 'Internet+Explorer',
    'VersionsList': 'HTTP%2F1.1',
    'MethodList': 'GET',
}



if __name__ == "__main__":
    while True:
        try:
            response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', json=data)
            proxies = response.text.split('\n')

            proxy = proxies[start].replace(' ', '').replace('\t', '').replace('\n', '')


            print(proxy)
            start += 1
            counter += 1
            

        except requests.exceptions.ConnectionError:
            print('requests.exceptions.ConnectionError: Check Your intetnet an try again')
