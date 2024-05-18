from collections import deque

# BFS
# cost = required min num of mirrors

def BFS(a, pstart, pend, graph, visited):
  deq = deque([pstart])
  graph[pstart[1]][pstart[0]] = -1
  while (deq):
    [cur_w, cur_h] = deq.popleft()
    cur_cost = graph[cur_h][cur_w]
    for i in range(cur_h - 1, -1, -1):
      if a[i][cur_w] == '*':
        break
      elif visited[i][cur_w] == 1 and cur_cost + 1 < graph[i][cur_w]:
        graph[i][cur_w] = cur_cost + 1
        deq.append([cur_w, i])
      elif visited[i][cur_w] == 0:
        graph[i][cur_w] = cur_cost + 1
        visited[i][cur_w] = 1
        deq.append([cur_w, i])

    for i in range(cur_h + 1, h, 1):
      if a[i][cur_w] == '*':
        break
      elif visited[i][cur_w] == 1 and cur_cost + 1 < graph[i][cur_w]:
        graph[i][cur_w] = cur_cost + 1
        deq.append([cur_w, i])
      elif visited[i][cur_w] == 0:
        graph[i][cur_w] = cur_cost + 1
        visited[i][cur_w] = 1
        deq.append([cur_w, i])

    for i in range(cur_w - 1, -1, -1):
      if a[cur_h][i] == '*':
        break
      elif visited[cur_h][i] == 1 and cur_cost + 1 < graph[cur_h][i]:
        graph[cur_h][i] = cur_cost + 1
        deq.append([i, cur_h])
      elif visited[cur_h][i] == 0:
        graph[cur_h][i] = cur_cost + 1
        visited[cur_h][i] = 1
        deq.append([i, cur_h])

    for i in range(cur_w + 1, w, 1):
      if a[cur_h][i] == '*':
        break
      elif visited[cur_h][i] == 1 and cur_cost + 1 < graph[cur_h][i]:
        graph[cur_h][i] = cur_cost + 1
        deq.append([i, cur_h])
      elif visited[cur_h][i] == 0:
        graph[cur_h][i] = cur_cost + 1
        visited[cur_h][i] = 1
        deq.append([i, cur_h])
  graph[pstart[1]][pstart[0]] = 0
  return graph[pend[1]][pend[0]]


w, h = map(int, input().split())
a = []
graph = [[987654321 for _ in range(w)] for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
pc = []  # [w, h]

for i in range(h):
  a.append(input())
  if 'C' in a[i]:
    for j in range(w):
      if 'C' == a[i][j]:
        pc.append([j, i])

min_cost = BFS(a, pc[0], pc[1], graph, visited)
print(min_cost)