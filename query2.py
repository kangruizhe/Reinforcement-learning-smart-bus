import pandas as pd
import numpy as np
import random



def q_net_make(finall):
    df = pd.read_csv('公交车.csv', encoding='cp936')
    a = len(df['公交车'])
    q = np.zeros((a, a))
    r = q
    # 建立 Q 表y
    x = finall
    b = []
    for i in range(a):
        if df['站点'][i] == x:
            b.append(i)
    # # 建立 R 表

    for i in range(a):
        for j in range(a):
            r[i][j] = 0
    for i in range(a):
        m = df['公交车'][i]
        # print(m)
        for j in range(a):
            if df['公交车'][j] == m:
                r[i][j] = 100 - df['流量'][j]
    for i in range(len(b)):
        for j in range(a):
            for k in range(a):
                if df['站点'][k] == x:
                    if df['公交车'][j] == df['公交车'][b[i]]:
                        r[j][k] = 2500

    e = []
    for i in range(a):
        m = df['站点'][i]
        d = []
        if i in e:
            continue
        for j in range(i, a):
            if df['站点'][j] == m:
                d.append(j)
                e.append(j)
        for k in range(len(d)):
            r[i] += r[d[k]]
        for k in range(len(d)):
            r[d[k]] = r[i]
    # r1=r
    for i in range(a):
        for j in range(a):
            if r[i][j] == 0:
                r[i][j] = -1
    gamma = 0.8
    # # 训练
    c = []
    d = []
    for i in range(100):  # 训练1000次
        # 对每一个训练,随机选择一种状态
        j = 0
        state = random.randint(0, a - 1)
        terro_state = state
        d.append(state)
        finall = x
        while (df['站点'][state] != finall):  # j!=50:#(state != finall)|(j!=50):
            # (这里就是每次episode，即每次尝试，直到5为止)
            # 选择r表中非负的值的动作
            if j >= 10:
                c.append(terro_state)
                break
            r_pos_action = []
            for action in range(a):
                if r[state, action] >= 0:
                    r_pos_action.append(action)
            next_state = r_pos_action[random.randint(0, len(r_pos_action) - 1)]
            q[state, next_state] = r[state, next_state] + gamma * q[next_state].max()
            state = next_state
            j = j + 1
    #

    e = [i for i in d if i not in c]
    e1=[]
   # print('请选择你的起点（输入地点前的数字即可）')
    for i in range(len(e)):
        e1.append(str(e[i])+"："+df['站点'][e[i]])
    return q,e1


def find(x,state,q):



    df = pd.read_csv('公交车.csv', encoding='cp936')
    a = len(df['公交车'])

    lucheng=[]
    jingdu=[]
    weidu=[]
    loca=[]


    # 验证
    # #int(input(':'))
    c1='起点处于'+df['站点'][state]
    # print('起点处于'+df['站点'][state])
    lucheng.append(c1)
    count = 0
    while df['站点'][state]!= x:
        if count > 10:
            print('失败')
            break
            # 选择最大的q_max
        q_max = q[state].max()
      #  print(q_max)
        q_max_action = []
        for action in range(a-1):
            if q[state, action] == q_max:
                q_max_action.append(action)
        #print(q_max_action)
        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        lujing="下一个地方去 " + df['站点'][next_state] + '，' +'乘坐公交车'+df['公交车'][state]
        #print("下一个地方去 " + df['站点'][next_state] + '，' +'乘坐公交车'+df['公交车'][next_state])
       # print(lujing)
        lucheng.append(lujing)
        jingdu.append(df['经度'][state])
        weidu.append(df['纬度'][state])
        loca.append(df['站点'][state])
        state = next_state
        count += 1
    jingdu.append(df['经度'][state])
    weidu.append(df['纬度'][state])
    loca.append(df['站点'][state])
    return lucheng,jingdu,weidu,loca

def show_road(j,w,l):
    import folium
    import os
    m = folium.Map([30.5076, 114.2352], zoom_start=10)  #中心区域的确定
    location=[]
    for i in range(len(j)):
        weizhi=[0,0]
        weizhi[0]=w[i]
        weizhi[1]=j[i]
        location.append(weizhi)
    # print(location)
    # print(l)
    # print(w)
    route = folium.PolyLine(    #polyline方法为将坐标用线段形式连接起来
        location,    #将坐标点连接起来
        weight=5,  #线的大小为3
        color='green',  #线的颜色为橙色
        opacity=0.8    #线的透明度
    ).add_to(m)    #将这条线添加到刚才的区域m内
    folium.Marker(location[0],
                  popup=str(l[0])+'(起点)',
                  icon=folium.Icon(color="red")).add_to(m)
    for i in range(1,len(w)-1):

        folium.Marker(location[i],
              popup=str(l[i]),icon=folium.Icon( color="blue")).add_to(m)
    folium.Marker(location[len(w) - 1],
                  popup=str(l[len(w) - 1])+'(终点)',
                  icon=folium.Icon( color="red")).add_to(m)
    m.save(os.path.join( r'D:\学习\毕业设计\项目\templates','geo_road.html'))  #将结果以HTML形式保存到桌面上




#
# q_net,first=q_net_make('鄂渚路文举街')
# mm,j,w,l=find('鄂渚路文举街',11,q_net)
# show_road(j,w,l)