# 使用urlleb获取百度首页
import urllib.request

# (1)定义一个url
url = "http://www.baidu.com"


# (2)模拟浏览器向服务器发送请求   response---响应
response = urllib.request.urlopen(url)
# (3)获取响应中的页面的源码   content--内容
# read方法 返回的是字节形式的二进制形式(开头有个b')
# 将二进制形式转换成字符串---解码---decode('编码的格式')---chaeset = utf-8
content = response.read().decode('utf-8')





print(content)
