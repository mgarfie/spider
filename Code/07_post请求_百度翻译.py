# 换个包装成为自己的软件(想法,有空自己做做试试)

import urllib.request
import urllib.parse
# post请求
# post地址
# https://fanyi.baidu.com/sug
url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'

}
data = {
    'kw': 'location',


}
# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')


# post的请求的参数 是不会放在url的后面的  而是需要放在request对象定制的参数中
# post请求的参数  必须要进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 字符串-->json对象

import json
obj = json.loads(content)
print(obj)

# 获取相应的数据

# ============================post与get的不同=========================================
# post请求方式的参数  必须编码,data = urllib.parse.urlencode(data).encode('utf-8')
# 编码之后必须调用encode方法
# 参数是放在请求对象定制的方法中request = urllib.request.Request(url=url, data=data, headers=headers)而不是像get一样连接到url后面





