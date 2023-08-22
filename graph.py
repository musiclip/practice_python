##함수
class Graph():
    def __init__(self, size):
        self.graph = [[0 for _ in range(size)] for _ in range(size)]




##변수
g1 = None
A,B,C,D = 0,1,2,3



##메인
g1 = Graph(4)
g1.graph[A][B] = 1; g1.graph[A][C] = 1; g1.graph[A][D] = 1
g1.graph[B][A] = 1; g1.graph[B][C] = 1; g1.graph[B][D] = 0
g1.graph[C][A] = 1; g1.graph[C][B] = 1; g1.graph[C][D] = 1
g1.graph[D][A] = 1; g1.graph[D][B] = 0; g1.graph[D][C] = 1

for i in range(4):
    for k in range(4):
        print(g1.graph[i][k], end = ' ')
    print()
