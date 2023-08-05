#from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import random

df=pd.read_csv('公交车.csv',encoding='cp936')
a=len(df['公交车'])

# 建立 Q 表y
q = np.zeros((a, a))
x=str(input("请输入终点:"))
#print(x)
b=[]
for i in range(a):
   #print(df['公交车'][i])
    if df['站点'][i]==x:
        b.append(i)

print(b)
# # 建立 R 表
#print(df['公交车'][55])
r=q
for i in range(a):
    for j in range(a):
        r[i][j]=0
for i in range(a):
    m=df['公交车'][i]
    #print(m)
    for j in range(a):
        if df['公交车'][j]==m:
            r[i][j]=100-df['流量'][j]
for i in range(len(b)):
        for j in range(a):
            for k in range(a):
                if df['站点'][k]==x:
                    if df['公交车'][j]==df['公交车'][b[i]]:
                        r[j][k]=2500

e=[]
for i in range(a):
    m = df['站点'][i]
    d=[]
    if i in e:

        continue
    for j in range(i,a):
        if df['站点'][j]==m:
                d.append(j)
                e.append(j)
    for k in range(len(d)):
        r[i]+=r[d[k]]
    for k in range(len(d)):
        r[d[k]]=r[i]
# r1=r
for i in range(a):
    for j in range(a):
        if r[i][j]==0:
            r[i][j]=-1
# for i in range(a):
#     m=df['站点'][i]
#     rw=r[i]
#     for j in range(a):
#         if i!=j:
#             if df['站点'][j]==m:
#                 rw+=r[j]
#     r1[i]=rw
#print(r[1])


# b1=r[b[0]]
# for i in range(len(b)):
#     for j in range(len(r[i])):
#         if r[b[i]][j]>=b1[i]:
#
#             b1[i]=r[b[i]][j]
# print(b1)
# for i in range(len(b)):
#     r[b[i]]=b1
# print(r[1])
# print(r[89])
# print(r[14])
# print(r[32])
#
# # for i in range(a):
# #     for j in range(a):
# #         if i==j:
# #             r[i][j]=0
# for i in range(a):
#     if df['公交车'][i]
#r[a-1][a-1]=100
# # a=df['公交车']
#print(r)
# print(r[20][20])
#print(r[55])







gamma = 0.8
# # 训练
c=[]
d=[]
c1=[]
d1=[]
r1=r
q1=q

for i in range(100): #训练1000次
    # 对每一个训练,随机选择一种状态
    j=0
    state = random.randint(0, a-1)
    terro_state=state
    d.append(state)
    finall=x

    while (df['站点'][state] != finall): #j!=50:#(state != finall)|(j!=50):
        #(这里就是每次episode，即每次尝试，直到5为止)
        # 选择r表中非负的值的动作
        if j>=10:
            c.append(terro_state)
            break
        r_pos_action = []
        for action in range(a):
            if r[state, action] >=0:
                r_pos_action.append(action)
        next_state = r_pos_action[random.randint(0, len(r_pos_action) - 1)]
        q[state, next_state] = r[state, next_state] + gamma * q[next_state].max()
        state = next_state
        j=j+1
#

e = [i for i in d if i not in c]
#print(q[4])
#print(len(c))
#print(len(d))
print(e)





for i in range(100): #训练100次
    # 对每一个训练,随机选择一种状态
    j=0
    state = e[random.randint(0, len(e)-1)]
    terro_state=state
    d1.append(state)
    finall=x

    while (df['站点'][state] != finall): #j!=50:#(state != finall)|(j!=50):
        #(这里就是每次episode，即每次尝试，直到5为止)
        # 选择r表中非负的值的动作
        if j>=10:
            c1.append(terro_state)
            break
        r_pos_action = []
        for action in range(a):
            if r1[state, action] >=0:
                r_pos_action.append(action)
        next_state = r_pos_action[random.randint(0, len(r_pos_action) - 1)]
        q1[state, next_state] = r1[state, next_state] + gamma * q1[next_state].max()
        state = next_state
        j=j+1
q=q1
r=r1
#
# for i in range(len(b)):
#     print(df['公交车'][b[i]])
# for i in range(len(c)):
#     print(df['公交车'][c[i]])

#
# #
# for i in range(a):
#     for j in range(a):
#         if q[i][j]<=0:
#             q[i][j]=0
#         q[i][j]=round(q[i][j],3)
#         q[i][j]=int(q[i][j])
# print(q[0][1])
# print(q[0].max())








#验证
# for i in range(100):
#     print("第{}次验证".format(i + 1))
#     state = e[random.randint(0, len(e)-1)]
#     print('起点处于'+df['站点'][state])
#     jiangli = df['流量'][state]
#     count = 0
#     while df['站点'][state]!= x:
#         if count > 20:
#             print('失败')
#             break
#         # 选择最大的q_max
#         q_max = q[state].max()琴台大道金龙路
#
#         q_max_action = []
#         for action in range(a):
#             if q[state, action] == q_max:
#                 q_max_action.append(action)
#
#         next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
#         # if
# #        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
#         print("下一个地方去 " + df['站点'][next_state] + '，' +'乘坐公交车'+df['公交车'][state])
#
#         state = next_state
#         jiangli += df['流量'][state]
#         count += 1
#     print("最终经过的流量："+str(jiangli))


















state =int(input(':'))
print('起点处于'+df['站点'][state])
jiangli=df['流量'][state]
count = 0
while df['站点'][state]!= x:
    if count > 10:
        print('失败')
        break
        # 选择最大的q_max
    q_max = q[state].max()
   # print(q_max)
    q_max_action = []
    for action in range(a):
        if q[state, action] == q_max:
            q_max_action.append(action)
    #print(q_max_action)
    next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
    print("下一个地方去 " + df['站点'][next_state] + '，' +'乘坐公交车'+df['公交车'][state])

    state = next_state
    count += 1
    jiangli += df['流量'][state]
print('总的流量是:' + str(jiangli))