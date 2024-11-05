# ***********************因版本更新已无法使用与运行，大致就是header中一个主要的cookin参数，将此参数带入到encode中就行了************************
import urllib.request

import urllib.parse



url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
#     'accept': 'text/event-stream',
#     # 'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'acs-token': '1730797655368_1730814200869_ww9U4OPcZ9xLAyoYmewxC1zcmDy/pv/hWc63lMXaKH5+iZqcE8XI1dTb+L2iDkRBsDKNhDJOAVO+Jq8kgMAk1Msxbv/bYK+P0N0JXZGk9L8XufTc5uZNGCH/28HDNMSyhlBZaPpD2f0Q1T3MjvcdomEhXS/2AQkMuwvMU0vl9SDrRIUAy8TJvGMpGvkfIuoEbu8pxaVHxxrqKCBSRBjeMzVQW+p+1KA0uikP0qh6Xy/m9FFH5714kHF8xops5vkkfbXHO8jr87UZjQiVKR3HuFy7yISWJDNZP23155fAXyP+CMLRsO+xkx2oc40XqgZ9mmEyiA9SBT9ZkNbdoUxtbcxEQmFrRaeRNWH7pMgiWI9cl+xCI6GP4MxRWLVtaFMnYqnUwXHTGQL6dZpUAN22/tA9gXcdq8dWMVVvHvnPiLMYcmIBgl7Tx5xhz2DIuOfVeM1zoHSTCf10YoCvp6S0ASgtIoxovdKvORdutg7WSN8=',
#     'connection': 'keep-alive',
#     'content-length': '139',
#     'content-type': 'application/json',
#     'cookie:BAIDUID=903B9344B95B9BC6CEBDEFCBB352E3EB:FG=1; BAIDUID_BFESS=903B9344B95B9BC6CEBDEFCBB352E3EB': 'FG=1; RT="z=1&dm=baidu.com&si=6f3cb7ee-e03c-431a-aa98-3a04b6858b3b&ss=m34i22n5&sl=4&tt=8zq&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; ab_sr=1.0.1_YTE1MmI0NWUyMjllNGQxZjI2NGExMmY5YTJmMDhmYmUzOWY3ZjY0NGJmZDMyMTdmNDJhMWRkM2I3YzQ5OTZlYWQzMmY4OWZjMWFkZWJmZTEyNzRiYzIyMTAyY2JkNjcwZjk4YjQ5ODhiNDA0ZmVhMjJkNzA5NDQ3OWFlYTkxYjk3MmE1M2E0MjVhMTYyNmM5OThjOTMxZGY5YzQwZWY3Mg==',
#     'host': 'fanyi.baidu.com',
#     'origin:https': '//fanyi.baidu.com',
#     'referer:https': '//fanyi.baidu.com/mtpe-individual/multimodal?query=spider&lang=en2zh&ext_channel=Aldtype',
#     'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#
#
#
# }

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': "realtime",
    'simple_means_flag':'3',
    'sign': '198772.518981',
    'token': '5483bfa652979b41f9c90d91f3de875d',
    'domain': 'common'

}

# post请求的参数必须要进行编码 并且要调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

import json
obj = json.loads(content)

print(obj)
