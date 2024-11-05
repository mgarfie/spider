# get请求
# 获取豆瓣电影第一页的数据 且保存起来
import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'

}

# (1) 请求对象的定制
request = urllib.request.Request(url, headers=headers)
# (2) 获取相应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# (3) 将数据下载都本地
# open方法默认使用gbk格式,若想保存中文则要指定为utf-8
fp = open('豆瓣第一页数据.json', 'w', encoding='utf-8')
fp.write(content)




























