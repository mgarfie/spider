import urllib.request

url = ('http://www.baidu.com')

# 模拟浏览器向服务器发送信息

response = urllib.request.urlopen(url)

# # 一个类型和六个方法
# response 是HTTPResponse类型
# print(type(response))    

# # 1按照一字节一字节读 效率慢
# content = response.read()  # read(数字代表返回几个字节,空为全部)
# print(content) 

# # 2按照一行读
# content = response.readline()
# print(content) 

# # 3按照一行读,直到读完
# content = response.readlines()
# print(content) 

# # 4返回状态码       如果是200证明没错，404一类的就为错
# print(response.getcode())


# # 5返回url地址
# print(response.geturl())

# # 6获取状态信息与响应头
# print(response.getheaders())
