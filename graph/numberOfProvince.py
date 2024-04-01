class Solution:
    def numProvinces(self, adj, V):
        adjL = {}
        for row in range(0, V):
            print("Hello")
            for col in range(0, V):
                if adj[row][col] == 1 and row != col:
                    if not adjL[row]:
                        adjL[row] = []
                        
                    if not adjL[col]:
                        adjL[col] = []
                        
                    adjL[row].append(col)
                    adjL[col].append(row)
          
        visited = [0] * V
        count = 0
        for i in range(0, V):
            if not visited[i]:
                count += 1
                dfs(i, adjL, visited)
                
        return count
            


def dfs(node, adjL, visited):
    visited[node] = 1
    neighbors = adjL[node]
    
    for el in neighbors:
        if visited[el]:
            continue
        visited[el] = 1
        dfs(el, adjL, visited)

