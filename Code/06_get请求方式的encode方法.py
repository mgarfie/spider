import urllib.request
import urllib.parse

# # urllencode使用场景:多个参数且都需要转换的情景
# # --------------------------------------------------------------------------------
# data = {
#     'wd':'周杰伦',
#     'sex':'男'
# }
# # 当多个情况下urlencode方法会将字典中的','转换为'&'为我们剩下大量精力
# a = urllib.parse.urlencode(data)
# print(a)
# # --------------------------------------------------------------------------------


# 获取网页源码
# https://cn.bing.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&local=%E5%8F%B0%E6%B9%BE
base_url = 'https://cn.bing.com/search?'
data = {
    'q': '周杰伦',
    'sex': '男',
    'local': '台湾'
}
new_data = urllib.parse.urlencode(data)
# print(new_data)

url = base_url + new_data

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'

}

# 请求对象的定制
request = urllib.request.Request(url, headers=headers)
# 模拟发请求
response = urllib.request.urlopen(request)
# 获取网页源码
content = response.read().decode('utf-8')
print(content)



