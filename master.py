import urllib.request
import urllib.parse
'''
url = 'http://www.baidu.com/'
response = urllib.request.urlopen(url)

print(response.read().decode())       # 测试url内容
print(response.geturl())              # 获取网页的url
print(response.getheaders())          # 获取网页头部（列表中元祖）
print(response.getcode())             # 获取相应码
print(response.readlines())           # 逐行读取

# # 获取url保存到文件
# with open('baidu.html','w',encoding='utf8') as fp:
#   fp.write(response.read().decode())
'''

# -------图片下载-------
'''
image_url = 'http://wanjia.object.com.cn/attachment/201007/13/23_1279012583U8KD.jpg'
response = urllib.request.urlopen(image_url)
# 保存图片1
with open('bz1.jpg', 'wb') as fp:
    fp.write(response.read())
# 保存图片2
urllib.request.urlretrieve(image_url, 'bz2.jpg')
'''

# -------模拟浏览器访问-------
'''
url = 'http://www.baidu.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36', }
request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request)
print(response.read().decode())
'''

# -------post-------
'''
url = 'https://fanyi.baidu.com/sug'
word = str(input("输入单词或汉字(英<-->中):"))
form_data = {'kw': word, }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36', }
request = urllib.request.Request(url=url, headers=headers)
form_data = urllib.parse.urlencode(form_data).encode()
response = urllib.request.urlopen(request, data=form_data)
print(response.read().decode())
'''

