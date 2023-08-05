# # # # from pyecharts import options as opts
# # # # from pyecharts.charts import Geo
# # # # from pyecharts.globals import ChartType, SymbolType, CurrentConfig
# # # #
# # # # CurrentConfig.ONLINE_HOST = 'https://assets.pyecharts.org/assets/'
# # # # # 链式调用
# # # #
# # # # c = Geo()
# # # # c.add_schema(
# # # #         maptype="china",
# # # #         itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
# # # #         label_opts=opts.LabelOpts(is_show=True)
# # # #     )
# # # # c.add(
# # # #         "",
# # # #         [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88), ('成都', 100), ('海口', 80)],
# # # #         type_=ChartType.EFFECT_SCATTER,
# # # #         color="white",
# # # #     )
# # # # c.add(
# # # #         "",
# # # #         [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆"),
# # # #          ('成都', '海口'), ('海口', '北京'), ('海口', '重庆'), ('重庆', '上海')
# # # #          ],
# # # #         type_=ChartType.LINES,
# # # #         effect_opts=opts.EffectOpts(
# # # #             symbol=SymbolType.ARROW, symbol_size=6, color="blue"
# # # #         ),
# # # #         linestyle_opts=opts.LineStyleOpts(curve=0.2),
# # # #     )
# # # # c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# # # # c.set_global_opts(title_opts=opts.TitleOpts(title="路线图"))
# # # # c.render("geo_lines_background.html")
# # #
# # # # c.render_notebook()
# # #
# # #
# # # from folium import plugins
# # # import folium
# # # import os
# # # m = folium.Map([39.1289, 117.3539], zoom_start=10)  #中心区域的确定
# # # location =[[39.1289, 117.3539], [39.1277262, 117.3542938], [39.1277275, 117.3543001], [39.1277262, 117.3542938],
# # #           [39.1277275, 117.3543001], [39.1277262, 117.3542938], [39.1277262, 117.3542938],
# # #           [39.1271896, 117.3541359], [39.127121, 117.354126], [39.127121, 117.354126],
# # #           [39.1269348, 117.3541107], [39.1268692, 117.3541061], [39.1263994, 117.3540649],
# # #           [39.1257591, 117.3540165], [39.125608, 117.3540192], [39.1251984, 117.3539717],
# # #           [39.1250038, 117.3539568], [39.1246886, 117.3539276], [39.1246033, 117.3539269],
# # #           [39.1244316, 117.353912], [39.1242828, 117.353912], [39.1241112, 117.3538971],
# # #           [39.1238623, 117.3538666], [39.1233153, 117.3538361], [39.1232643, 117.3538374],
# # #           [39.1230354, 117.3537478], [39.1229895, 117.353714], [39.1228638, 117.3535239], [39.122818, 117.3534493],
# # #           [39.1227334, 117.353241], [39.1226985, 117.3531494], [39.122652, 117.3530273], [39.122652, 117.3529968],
# # #           [39.1225821, 117.352829], [39.1225239, 117.3526764], [39.1224861, 117.3525835], [39.1224774, 117.3525391],
# # #           [39.1224657, 117.3525238], [39.1224174, 117.3523745], [39.1221886, 117.3517625], [39.1221771, 117.3517327],
# # #           [39.1221399, 117.3516388], [39.1221199, 117.3515834], [39.1220169, 117.3512998], [39.1219769, 117.3512115],
# # #           [39.1219482, 117.3511057], [39.1219188, 117.3510437], [39.121814, 117.3507996], [39.1217791, 117.3507385],
# # #           [39.1217558, 117.350708], [39.1215935, 117.3505982], [39.121558, 117.3505859], [39.1213417, 117.3506131],
# # #           [39.1211014, 117.3507475], [39.121011, 117.3507996], [39.1209528, 117.3508301], [39.120883, 117.3508759],
# # #           [39.1208481, 117.3509064], [39.1207352, 117.3509714], [39.1204834, 117.3511356], [39.120369, 117.3511953],
# # #           [39.120369, 117.3511953], [39.1202774, 117.351255], [39.1186409, 117.3522551], [39.1185321, 117.3523254],
# # #           [39.1182976, 117.3524641], [39.1181374, 117.3525686], [39.1173566, 117.3530426], [39.1171188, 117.3531955],
# # #           [39.1168213, 117.3533746], [39.1163325, 117.3536682], [39.115867, 117.3539581], [39.1156691, 117.3540802],
# # #           [39.1156342, 117.3540955], [39.1156342, 117.3540955], [39.1144981, 117.3547927], [39.113551, 117.3553772],
# # #           [39.113551, 117.3553772], [39.1125069, 117.3559869], [39.1120846, 117.3557129], [39.1120846, 117.3557129],
# # #           [39.1119118, 117.3553002], [39.1118546, 117.355136], [39.111782, 117.3549652], [39.1115456, 117.3542404],
# # #           [39.1115958, 117.3540649], [39.1115958, 117.3540649], [39.1128411, 117.3532562], [39.1131786, 117.3530426],
# # #           [39.113807, 117.3526459], [39.113807, 117.3526459], [39.1191902, 117.3493593], [39.1197308, 117.3490295],
# # #           [39.1206386, 117.3484802], [39.1208713, 117.3483276], [39.1214676, 117.347971], [39.1214676, 117.347971],
# # #           [39.1214676, 117.347971], [39.1214676, 117.347971]]   #输入坐标点（注意）folium包要求坐标形式以纬度在前，经度在后
# # # route = folium.PolyLine(    #polyline方法为将坐标用线段形式连接起来
# # #     location,    #将坐标点连接起来
# # #     weight=3,  #线的大小为3
# # #     color='orange',  #线的颜色为橙色
# # #     opacity=0.8    #线的透明度
# # # ).add_to(m)    #将这条线添加到刚才的区域m内
# # # m.save(os.path.join('Heatmap1.html'))  #将结果以HTML形式保存到桌面上
# # # a=[100,1001,10001,100001]
# # # b=[200,2000,3000,4000]
# # #
# # # location =[]
# # # for i in range(len(a)):
# # #     c=[0,0]
# # #     c[0]=a[i]
# # #     c[1]=b[i]
# # #     location.append(c)
# # #     # location[i][0]=a[i]
# # #     # location[i][1]=b[i]
# # # print(location)
# #
# # # import numpy as np
# # # import random
# # # # 建立 Q 表
# # # q = np.zeros((6, 6))
# # # # 建立 R 表
# # # r = np.array([[-1, -1, -1, -1, 0, -1],
# # #               [-1, -1, -1, 0, -1, 100],
# # #               [-1, -1, -1, 0, -1, -1],
# # #               [-1, 0, 0, -1, 0, -1],
# # #               [0, -1, -1, 0, -1, 100],
# # #               [-1, 0, -1, -1, 0, 100]])
# # # # 衰减指数
# # # gamma = 0.7
# # # # 训练
# # # for i in range(1000): #训练1000次
# # #     # 对每一个训练,随机选择一种状态
# # #     state = random.randint(0, 5)
# # #     while state != 5:#(这里就是每次episode，即每次尝试，直到5为止)
# # #         # 选择r表中非负的值的动作
# # #         r_pos_action = []
# # #         for action in range(6):
# # #             if r[state, action] >= 0:
# # #                 r_pos_action.append(action)
# # #         next_state = r_pos_action[random.randint(0, len(r_pos_action) - 1)]
# # #         q[state, next_state] = r[state, next_state] + gamma * q[next_state].max()
# # #         state = next_state
# # # print(q)
# # # 验证
# # import folium
# # import os
# #
# # location=[[30.52201, 114.219023], [30.504171, 114.203498], [30.507014, 114.206836], [30.50622, 114.206107], [30.508751, 114.231758], [30.507504, 114.235153]]
# # m = folium.Map([30.5076, 114.2352], zoom_start=10)
# # l=['梅林西路梅林三街', '春晓路蔷薇路', '蔷薇路永旺梦乐城', '蔷薇路永旺梦乐城', '鄂渚路文举街', '国际博览中心公交场站']
# # w=[30.52201, 30.504171, 30.507014, 30.50622, 30.508751, 30.507504]
# # route = folium.PolyLine(    #polyline方法为将坐标用线段形式连接起来
# #         location,    #将坐标点连接起来
# #         weight=5,  #线的大小为3
# #         color='green',  #线的颜色为橙色
# #         opacity=0.8    #线的透明度
# #     ).add_to(m)    #将这条线添加到刚才的区域m内
# # folium.Marker(location[0],
# #                   popup=str(l[0])+'(起点)',
# #                   icon=folium.Icon(color="red")).add_to(m)
# # for i in range(1,len(w)-1):
# #
# #         folium.Marker(location[i],
# #               popup=str(l[i]),icon=folium.Icon( color="blue")).add_to(m)
# #
# # folium.Marker(location[len(w) - 1],
# #                   popup=str(l[len(w) - 1])+'(终点)',
# #                   icon=folium.Icon( color="red")).add_to(m)
# # m.save(os.path.join( 'o_road.html'))  #将结果以HTML形式保存到桌面上
# # import pandas as pd
# # df=pd.read_csv('公交车.csv',encoding='cp936')
# # f = open('站点信息.txt', 'w')
# # for i in df['站点']:
# #     f.write(i+'   ')
# # f.close()
# import numpy as np
# import random
#
# # 建立 Q 表
# q = np.zeros((6, 6))
# q = np.matrix(q)
#
# # 建立 R 表
#
# r = np.array([[-1, -1, -1, -1, 0, -1], [-1, -1, -1, 0, -1, 100], [-1, -1, -1, 0, -1, -1], [-1, 0, 0, -1, 0, -1],
#               [0, -1, -1, 0, -1, 100], [-1, 0, -1, -1, 0, 100]])
# r = np.matrix(r)
#
# # 贪婪指数
# gamma = 0.8
#
# # 训练
#
# for i in range(100):
#     # 对每一个训练,随机选择一种状态
#     state = random.randint(0, 5)
#     while state != 5:
#         # 选择r表中非负的值的动作
#         actions = []
#         for a in range(6):
#             if r[state, a] >= 0:
#                 actions.append(a)
#         action = actions[random.randint(0, len(actions) - 1)]
#         print(actions)
#         R = r[state, action]
#
#         next_state = action
#         actions = []
#         for a in range(6):
#             if r[next_state, a] >= 0:
#                 actions.append(a)
#
#         next_action = actions[random.randint(0, len(actions) - 1)]
#         q[state, action] = R + gamma * q[next_state, next_action]
#
#         state = next_state
#         action = next_action
#
# print(q)
# # 验证
#
# # for i in range(10):
# #     print("第{}次验证".format(i + 1))
# #
# #     state = random.randint(0, 2)
# #     print('机器人处于{}'.format(state))
# #     count = 0
# #     while state != 5:
# #         if count > 20:
# #             print('fail')
# #             break
# #         # 选择最大的q_max
# #         q_max = q[state].max()
# #
# #         q_max_action = []
# #         for action in range(6):
# #             if q[state, action] == q_max:
# #                 q_max_action.append(action)
# #
# #         next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
# #         print("the robot goes to " + str(next_state) + '.')
# #         state = next_state
# #         count += 1




# import query_sarsa as qu
# q,e1,e=qu.sarsa_net_make('鄂渚路文举街')
# tureq=qu.sarsa_true_net(e,'鄂渚路文举街')
# l,j,w,lo=qu.sarsa_find('鄂渚路文举街',83,tureq)
# qu.sarsa_show_road(j,w,l)



a=[97, 325, 241, 7, 474, 378, 435, 0, 215, 174, 409, 73, 59, 156, 524, 11]
print(a[1])