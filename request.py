import requests
import json
import hashlib
import time


def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


url = "https://area12-win.pospal.cn:443/pospal-api2/openapi/v1/ticketOpenApi/queryTicketPages"
appKey = "883812324873092589"
appId = "8B32F5B404D9D0AC5B42ACCC9015FEE5"

jsonData = json.dumps({
    'appId' : appId,
    'startTime' : '2017-11-30 00:00:01',
    'endTime' : '2017-11-30 23:59:59',
})

signature = get_md5(appKey + jsonData).upper()

headers = {
    'User-Agent' : 'openApi',
    'Content-Type' : 'application/json; charset=utf-8',
    'accept-encoding' : 'gzip,deflate',
    'time-stamp': str(int(time.time())),
    'data-signature' : signature
}
result = requests.post(url, data=jsonData, headers = headers, verify=False)
print (result)
# print (result.content)
print (result.text)
