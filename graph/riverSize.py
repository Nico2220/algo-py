def riverSizes(matrix):
    result = []
    visited = [[False for value in row] for row in matrix]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0 or visited[i][j] == True:
                continue
            bfs(i, j, matrix, visited, result)
    return result
            
            
def bfs(i, j, matrix, visited, result):
    size = 0
    queue = [[i,j]]
    visited[i][j] = True
    while(len(queue) > 0):
        current = queue.pop()
        size  = size + 1
        neighbors = getNeighbors(current, matrix, visited)
        for neighbor in neighbors:
            if matrix[neighbor[0]] [neighbor[1]] == 1:
                queue.append(neighbor)
                visited[neighbor[0]][neighbor[1]] = True
    if size > 0:
        result.append(size)

def getNeighbors(currentPosition, matrix, visited):
    neighbors = []
    i = currentPosition[0]
    j = currentPosition[1]
    
    if i > 0 and visited[i-1][j] == False:
        neighbors.append([i - 1, j])
    if i < len(matrix) - 1 and visited[i][j] == False:
        neighbors.append([i+1, j])
    if j > 0 and visited[i][j - 1] == False:
        neighbors.append([i, j-1])
    if j < len(matrix[i])  - 1 and visited[i][j + 1] == False:
        neighbors.append([i, j+1])

    return neighbors


print(riverSizes([
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]))