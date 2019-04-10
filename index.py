import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

class ProxySpider:
    def run(self):
        while True:
            self.debug('Start to grab proxy from ' + os.getenv('API_URL'))

            # get proxy
            headers = {'X-API-KEY': os.getenv('API_KEY')}
            payload = {'format': 'txt'}
            response = requests.post(os.getenv('API_URL'), data=payload, headers=headers)

            # store proxy
            f = open('shared/proxy.txt', 'w+')
            f.write(response.text)
            f.close()

            self.debug('Proxy grabbed successfully')

            # sleep between next interval
            time.sleep(int(os.getenv('REQUEST_INTERVAL', 60)))

    def debug(self, msg):
        if (os.getenv('DEBUG') == 'True'):
            print(msg)

if __name__ == '__main__':
    spider = ProxySpider()
    spider.run()
