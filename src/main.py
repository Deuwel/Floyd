#Floyd 알고리즘으로 건물 간 최단경로 구하기
import math

INF = math.inf
GREEN = "\033[92m"
RST = "\033[0m" 

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
def print_mat(mat, updated, node, title=None):
    CELLWIDTH = 5
    if title:
        print(f"\n====={title}=====")
    print(" " + " ".join(f"{n:>5}" for n in node))

    for i, row in enumerate(mat):
        line = f"{node[i]:>3} "
        row_str = []
        for j, val in enumerate(row):
            if val == INF:
                cell = f"{'INF':>{CELLWIDTH}}"
            else:
                cell = f"{val:>{CELLWIDTH}}"

            if updated[i][j] == True:
                line += GREEN + cell + RST
            else:
                line += cell + " "
        print(line)
    print()


#모든 정점 간 최단경로 구하기
def distance_floyd(vertex, distMap):
    rep = len(distMap)
    print_mat(distMap, [[False]*rep for _ in range(rep)], vertex, title="초기 행렬")

    for k in range(rep):
        updated_Matrix = [[False]*rep for _ in range(rep)]
        for i in range(rep):
            for j in range(rep):
                if distMap[i][j] > distMap[i][k] + distMap[k][j]:
                    updated_Matrix[i][j] = True
                distMap[i][j] = min(distMap[i][j], distMap[i][k]+distMap[k][j])

        print_mat(distMap, updated_Matrix, vertex, title=f"정점 {vertex[k]} 사용 후")
    print_mat(distMap, [[False]*rep for _ in range(rep)], vertex, title="최종 최단경로 행렬")

distance_floyd(building,dist)


