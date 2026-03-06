#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
解答问题1：从出入口出发，游玩5个主题乐园，找出步行时间最短的路线。

根据OCR识别出的图片数据，构建步行时间图。
地点坐标(从图中)：
  - 出入口: 左下方
  - 明日世界: 左上方
  - 皮克斯玩具总动员: 中上方
  - 梦幻世界: 右上方
  - 奇想花园: 中间
  - 宝藏湾: 右下方
  - 探险岛: 中下方

从两张图片OCR数据中提取的步行时间（分钟）:
图1(第一张): 
  出入口附近: 6分钟, 11分钟(II分)
  奇想花园附近: 5分钟, 6分钟, 4分钟
  皮克斯玩具总动员附近: 11分钟, 14分钟
  宝藏湾附近: S(5)分钟, 6分钟
  梦幻世界附近: 14分钟

图3(第三张图，更清晰的地图):
  位置关系和数值更清楚
  出入口(左下) - 明日世界(左上): 11分钟
  出入口 - 奇想花园: 6分钟 or 5分钟
  出入口 - 探险岛: 19分钟
  明日世界 - 奇想花园: 7分钟
  明日世界 - 皮克斯玩具总动员: 11分钟
  皮克斯玩具总动员 - 梦幻世界: 14分钟
  皮克斯玩具总动员 - 奇想花园: 14分钟
  奇想花园 - 梦幻世界: 4分钟  
  奇想花园 - 探险岛: 6分钟
  奇想花园 - 宝藏湾: 6分钟
  梦幻世界 - 宝藏湾: 5分钟
  宝藏湾 - 探险岛: 4分钟(?)
  出入口 - 宝藏湾: 可能需要经由其他点
"""

from itertools import permutations

# 根据OCR数据和上海迪士尼的实际地图布局，构建步行时间图
# 节点: 0=出入口, 1=宝藏湾, 2=梦幻世界, 3=明日世界, 4=奇想花园, 5=探险岛
# (皮克斯玩具总动员不在问题1的5个乐园中，所以不需要访问)

# 邻接矩阵 (单位：分钟)
# 999 表示不直接连通（需要经过其他节点）
INF = 999
names = ["出入口", "宝藏湾", "梦幻世界", "明日世界", "奇想花园", "探险岛"]

# 根据图片OCR数据构建的距离矩阵
#           出入口  宝藏湾  梦幻世界  明日世界  奇想花园  探险岛
dist = [
    #出入口
    [0,     INF,    INF,    11,     6,      9],
    #宝藏湾
    [INF,   0,      5,      INF,    6,      4],
    #梦幻世界
    [INF,   5,      0,      INF,    4,      INF],
    #明日世界
    [11,    INF,    INF,    0,      7,      INF],
    #奇想花园
    [6,     6,      4,      7,      0,      5],
    #探险岛
    [9,     4,      INF,    INF,    5,      0],
]

# 先用Floyd-Warshall计算所有点对之间的最短距离
n = len(names)
shortest = [row[:] for row in dist]
path_via = [[None]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if shortest[i][k] + shortest[k][j] < shortest[i][j]:
                shortest[i][j] = shortest[i][k] + shortest[k][j]
                path_via[i][j] = k

print("各点之间最短距离矩阵:")
print(f"{'':10s}", end="")
for name in names:
    print(f"{name:8s}", end="")
print()
for i in range(n):
    print(f"{names[i]:10s}", end="")
    for j in range(n):
        print(f"{shortest[i][j]:8d}", end="")
    print()

# 问题1: 从出入口(0)出发，访问 宝藏湾(1)、梦幻世界(2)、明日世界(3)、奇想花园(4)、探险岛(5)
# 最后回到出入口(0)
# 穷举所有排列
must_visit = [1, 2, 3, 4, 5]  # 5个乐园

print(f"\n{'='*60}")
print("穷举所有路线 (出入口 -> 5个乐园 -> 出入口)")
print(f"{'='*60}")

best_time = INF
best_route = None
all_routes = []

for perm in permutations(must_visit):
    route = [0] + list(perm) + [0]
    total = 0
    for i in range(len(route)-1):
        total += shortest[route[i]][route[i+1]]
    all_routes.append((total, route))
    if total < best_time:
        best_time = total
        best_route = route

# 排序输出前10条最优路线
all_routes.sort(key=lambda x: x[0])

print(f"\n前10条最短路线:")
for idx, (time, route) in enumerate(all_routes[:10]):
    route_str = " -> ".join(names[r] for r in route)
    marker = " ★ 最优" if idx == 0 else ""
    print(f"  {idx+1}. {route_str}")
    print(f"     总步行时间: {time} 分钟{marker}")

print(f"\n{'='*60}")
print(f"★ 最优路线:")
route_str = " -> ".join(names[r] for r in best_route)
print(f"  {route_str}")
print(f"  总步行时间: {best_time} 分钟")
print(f"\n  详细分段:")
for i in range(len(best_route)-1):
    a, b = best_route[i], best_route[i+1]
    print(f"  {names[a]} -> {names[b]}: {shortest[a][b]} 分钟")

