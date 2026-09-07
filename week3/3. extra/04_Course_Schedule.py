from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = [[], 0]
        
        for current, prev in prerequisites:
            if current == prev:
                return False
            graph[current][1] += 1
            graph[prev][0].append(current)

        queue = deque([node for node in graph if graph[node][1] == 0])

        result = 0

        while(queue):
            temp = queue.popleft()
            result += 1
            for i in graph[temp][0]:
                graph[i][1] -= 1
                if graph[i][1] == 0:
                    queue.append(i)

        return result == numCourses


        

            
            