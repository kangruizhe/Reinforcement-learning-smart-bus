import pandas as pd
df1=pd.read_csv('a.csv',encoding='cp936')
import requests
import json
from bs4 import BeautifulSoup
import random
# 定义一个函数，传入线路名称相当于在高德地图搜索，来获取每趟公交的站点名称和经纬度
def get_location(line):
    a=[]
    url_api = 'https://restapi.amap.com/v3/bus/linename?s=rsv3&extensions=all&key=559bdffe35eec8c8f4dae959451d705c&output=json&city=武汉&offset=2&keywords={}&platform=JS'.format(
        line)
    res = requests.get(url_api).text
    # print(res) 可以用于检验传回的信息里面是否有自己需要的数据
    rt = json.loads(res)
    # print(rt)
    # print(rt['buslines'])
    i = 0
    line_name = rt['buslines'][0]['name']
    polyline = rt['buslines'][0]['polyline']
    info = [line_name, polyline]

    #print(info)
    stop = rt['buslines'][0]['busstops']
    #print(line)
    for i in range(len(stop)):
        station = stop[i]['name']
        # a.append(line)
        location = stop[i]['location']
        #b.append(location)
        info_ = [line, station, location]
        a.append(info_)
        #print(info_)
        i += 1
    return a

url = "https://wuhan.8684.cn/line3"  # 今天就只先演示获取一种线路类型下所有公交的信息，要想拿到整个城市的，其实就加个for循环:line1,line2,line3......
# 伪装请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
# 通过requests模块模拟get请求
res = requests.get(url=url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")
div = soup.find('div', class_='list clearfix')
lists = div.find_all('a')
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
for item in lists:
    line = item.text  # 获取a标签下的公交线路
    b.append(get_location(line))
for i in range(21):
    for j in range(len(b[i])):
        rad=random.randint(1,100)
        c.append(b[i][j][0])
        d.append(b[i][j][1])
        e.append(b[i][j][2].split(',')[0])
        f.append(b[i][j][2].split(',')[1])
        h.append(rad)
        lng=float(b[i][j][2].split(',')[0])
        lat=float(b[i][j][2].split(',')[1])
        dict_data = dict(lng=lng, lat=lat, count=rad)
        g.append(dict_data)

#print(b[0][0][2].split(',')[0])
df1['公交车']=c
df1['站点']=d
df1['经度']=e
df1['纬度']=f
df1['流量']=h

df1.to_csv('公交车.csv',encoding='cp936')
f = open('经纬度信息.txt', 'w')
f.write(json.dumps(g))

f.close()
print('数据生成完毕')