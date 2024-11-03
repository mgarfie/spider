import urllib.request

# 故意创建一个错误https
url = 'https://www.baidu.com'


# url 的组成 1.协议(http:80/https:443)  
#  2.主机(域名)   3.端口号mysql3306,oracle 1521,mongodb 27017 #4.路径 5.参数 6.锚点
# https/http   www.baidu.com /             s?        wd=周杰伦
#    协议      主机            :80端口号    s路径        wd参数

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'

}

# 因为urlopen方法中不能存储字典,因此headers不能传入进去 创建为一个request对象
# 请求对象的定制
# 注意 因为参数顺序问题,不能直接写url和hearder,中间还有data参数,因此使用关键字传参
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)


content = response.read().decode('utf8')
print(content)                                        # 此时发现数据不完整,反爬(UA user agent为用户代理,包含一些信息)

# UA介绍:User Agent中文名为用户代理，简称 UA，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、
# CPU 类型、浏览器及版本。浏览器内核、浏览器渲染引擎、浏览器语言、浏览器插件等
 