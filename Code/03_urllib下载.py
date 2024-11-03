import urllib.request

url_netpage = 'http://www.baidu.com'
# 下载网页  默认下载到根目录
urllib.request.urlretrieve(url_netpage, 'baidu.html')
# 下载图片
url_img = 'https://wx3.sinaimg.cn/mw690/006lSKKBly1hv6hd4378nj30u01bzwmf.jpg'

urllib.request.urlretrieve(url= url_img, filename='weibo.jpg')
# 下载视频

url_vidio = 'http://t.cn/A6niNf3P'
