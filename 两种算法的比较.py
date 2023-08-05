# #from flask import Flask, request, render_template



def find_ture_first():
    # 贪婪指数
    import pandas as pd
    import numpy as np
    import random

    df = pd.read_csv('公交车.csv', encoding='cp936')
    a = len(df['公交车'])

    # 建立 Q 表y
    q = np.zeros((a, a))
    x = str(input("请输入终点:"))
    # print(x)
    b = []
    for i in range(a):
        # print(df['公交车'][i])
        if df['站点'][i] == x:
            b.append(i)

   # print(b)
    # # 建立 R 表
    # print(df['公交车'][55])
    r = q
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
    for i in range(a):
        for j in range(a):
            if r[i][j] == 0:
                r[i][j] = -1
    gamma = 0.8

    # 训练
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
    e = [i for i in d if i not in c]
    # e=e.sort()
    # print(q[4])
    # print(len(c))
    # print(len(d))
    return e,x


def q_learning(e1,finall):
    import pandas as pd
    import numpy as np
    import random
    gamma = 0.8
    df = pd.read_csv('公交车.csv', encoding='cp936')
    a = len(df['公交车'])

    # 建立 Q 表y
    q = np.zeros((a, a))
    x = finall#str(input("请输入终点:"))
    # print(x)
    b = []
    for i in range(a):
        # print(df['公交车'][i])
        if df['站点'][i] == x:
            b.append(i)

   # print(b)
    # # 建立 R 表
    # print(df['公交车'][55])
    r = q
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
    for i in range(a):
        for j in range(a):
            if r[i][j] == 0:
                r[i][j] = -1
    c = []
    d = []
    for i in range(100):  # 训练100次
        # 对每一个训练,随机选择一种状态
        j = 0
        state = e1[random.randint(0, len(e1) - 1)]
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
    return q





def sarsa(e1,finall):
    import pandas as pd
    import numpy as np
    import random
    gamma = 0.8
    df = pd.read_csv('公交车.csv', encoding='cp936')
    a = len(df['公交车'])

    # 建立 Q 表y
    q = np.zeros((a, a))
    x = finall  # str(input("请输入终点:"))
    # print(x)
    b = []
    for i in range(a):
        # print(df['公交车'][i])
        if df['站点'][i] == x:
            b.append(i)

   # print(b)
    # # 建立 R 表
    # print(df['公交车'][55])
    r = q
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
    for i in range(a):
        for j in range(a):
            if r[i][j] == 0:
                r[i][j] = -1
    c = []
    d = []
    for i in range(100):  # 训练1000次
        # 对每一个训练,随机选择一种状态
        j = 0
        state = e1[random.randint(0, len(e1) - 1)]
        terro_state = state
        d.append(state)
        finall = x

        while (df['站点'][state] != finall):  # j!=50:#(state != finall)|(j!=50):
            # (这里就是每次episode，即每次尝试，直到5为止)
            # 选择r表中非负的值的动作
            if j >= 10:
                c.append(terro_state)
                break
            actions = []
            for li in range(a):
                if r[state, li] >= 0:
                    actions.append(li)
            action = actions[random.randint(0, len(actions) - 1)]
            R = r[state, action]
            next_state = action
            actions = []
            for lt in range(a):
                if r[next_state, lt] >= 0:
                    actions.append(lt)
            # 采取相同的动作（sa1rsa核心）
            next_action = actions[random.randint(0, len(actions) - 1)]
            q[state, action] = R + gamma * q[next_state, next_action]

            state = next_state
            action = next_action
            j = j + 1
    return q
def contrast(e1,q1,q2,final):
    import pandas as pd
    import numpy as np
    import random
    # gamma = 0.8
    df = pd.read_csv('公交车.csv', encoding='cp936')
    a = len(df['公交车'])

    print('下面开始对比五条路线：')
    # print(e1)
    for i in range(5):

        state1 =e1[i]
        print('(Q-learning)起点处于'+df['站点'][state1])
        count1 = 0
        jiangli1 = df['流量'][state1]
        while df['站点'][state1] != final:
            if count1 > 10:
                print('失败')
                break
                # 选择最大的q_max
            q_max1 = q1[state1].max()
            # print(q_max)
            q_max_action1 = []
            for action in range(a):
                if q1[state1, action] == q_max1:
                    q_max_action1.append(action)
            # print(q_max_action)
            next_state1 = q_max_action1[random.randint(0, len(q_max_action1) - 1)]
            print("下一个地方去 " + df['站点'][next_state1] + '，' + '乘坐公交车' + df['公交车'][state1])

            state1 = next_state1
            count1 += 1
            jiangli1 += df['流量'][state1]
        print('总的流量是:' + str(jiangli1))

        state2 = e1[i]
        print('(sarsa)起点处于' + df['站点'][state2])
        jiangli2 = df['流量'][state2]
        count2=0
        while df['站点'][state2] != final:
            if count2 > 10:
                print('失败')
                break
                # 选择最大的q_max
            q_max2 = q2[state2].max()
            # print(q_max)
            q_max_action2 = []
            for action in range(a):
                if q2[state2, action] == q_max2:
                    q_max_action2.append(action)
            # print(q_max_action)
            next_state2 = q_max_action2[random.randint(0, len(q_max_action2) - 1)]
            print("下一个地方去 " + df['站点'][next_state2] + '，' + '乘坐公交车' + df['公交车'][state2])

            state2 = next_state2
            count2 += 1
            jiangli2 += df['流量'][state2]
        print('总的流量是:' + str(jiangli2))
        print(' ')
        print(' ')

e1,finall=find_ture_first()
#print(e1)
q1=q_learning(e1,finall)
q2=sarsa(e1,finall)
contrast(e1,q1,q2,finall)