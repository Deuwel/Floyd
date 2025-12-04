#Floyd 알고리즘으로 건물 간 최단경로 구하기
import math

INF = math.inf
building = ['A','B','C','D','E','F','G']
dist = [[0, 94, 100, 98, INF, INF, INF],
        [94, 0, INF, 80, 113, INF, INF],
        [100, INF, 0, INF, INF, INF, 87],
        [98, 80, INF, 0, 74, INF, 63],
        [INF, 113, INF, 74, 0, 135, INF],
        [INF ,INF, INF, INF, 135, 0, 119],
        [INF, INF, 87, 63, INF, 119, 0]
]

#행렬 출력 함수
def print_mat(mat, node, title=None):
    if title:
        print(f"\n====={title}=====")
    print("   " + " ".join(f"{n:>5}" for n in node))

    for i, row in enumerate(mat):
        row_str = []
        for val in row:
            if val == INF:
                row_str.append(" INF ")
            else:
                row_str.append(f"{val:>5}")
        print(f"{node[i]:>3} "+" ".join(row_str))
    print()


#모든 정점 간 최단경로 구하기
def distance_floyd(vertex, distMap):
    rep = len(distMap)
    for k in range(rep):
        for i in range(rep):
            for j in range(rep):
                distMap[i][j] = min(distMap[i][j], distMap[i][k]+distMap[k][j])
        print_mat(distMap, vertex, title=f"정점 {vertex[k]} 사용 후")
    print_mat(distMap, vertex, title="최종 최단경로 행렬")

distance_floyd(building,dist)


