import urllib.request
import urllib.parse
# url1 = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
# url2 = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20'
# url3 = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20'
# url4 = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=60&limit=20'

#            第1/2/3/4/5/6/7/8...页
# 寻找规律:star=0/20/40/60/80
# start = (page-1)*20

# (1) 请求对象的定制


# (2) 获取相应的数据
# (3) 将数据下载都本地

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

    data = {
        'start': (page - 1) * 20,
        'limit': 20,
    }
    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'

    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):

    with open('豆瓣'+ str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)



if __name__ == '__main__':
    start_page = int(input('请输入起始的号码'))
    end_page = int(input('请输入结束的号码'))
    for page in range(start_page, end_page+1):
        # 每一页都有自己请求对象的定制
        request = create_request(page)
        # 获取相应的数据
        content = get_content(request)
        # 下载相应的数据
        down_load(page, content)






























