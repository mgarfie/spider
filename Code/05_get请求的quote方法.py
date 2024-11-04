import urllib.request
import urllib.parse

# https://cn.bing.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6   q=‘后面的就为周杰伦的unicode码’

# 获取地址

url = 'https://cn.bing.com/search?q='

# 请求对象定制，是为了解决反扒的一种手段
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'

}
# 将周杰伦文字变成unicode编码的格式  我们需要用一个urill.parse的功能
name = urllib.parse.quote_plus('周杰伦')
url = url + name
print(url)
# 请求对象的定制

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')
print(content)
