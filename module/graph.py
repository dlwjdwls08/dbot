from typing import Literal
import math, sys

class Graph:
    def __init__(self):
        self.graph = {}
        self.default_value = None
    def __getitem__(self,pos:list[int,int]):
        if type(pos) != tuple: raise Exception("Graph[x(int), y(int)]")
        if len(pos) != 2: raise Exception("Graph[x(int), y(int)]")
        if type(pos[0]) != int or type(pos[1]) != int: raise Exception("Graph[x(int), y(int)]")
        if not pos in self.graph:
            self.graph[pos] = self.default_value
        return self.graph[pos]
    def __setitem__(self,pos:list[int,int],value):
        if type(pos) != tuple: raise Exception("Graph[x(int), y(int)]")
        if len(pos) != 2: raise Exception("Graph[x(int), y(int)]")
        if type(pos[0]) != int or type(pos[1]) != int: raise Exception("Graph[x(int), y(int)]")
        self.graph[pos] = value
        return value
    def __iter__(self):
        return iter(self.graph)
    def fill(self,value):
        self.default_value = value
        for pos in self.graph:
            self.graph[pos] = self.default_value
    def fill_area(self,left_top:list[int,int],left_bottom:list[int,int],right_bottom:list[int,int],right_top:list[int,int],value):
        if not (left_top[0] == left_bottom[0] and left_bottom[1] == right_bottom[1] and right_bottom[0] == right_top[0] and right_top[1] == left_top[1]):
            raise Exception('parameter is not available')
        for x in range(left_bottom[0],right_bottom[0]+1):
            for y in range(left_bottom[1],left_top[1]+1):
                self.graph[x,y] = value
    def replace(self,target_value,value) -> Literal['changed pos']:
        changed_pos = []
        for pos in self.graph:
            if self.graph[pos] == target_value:
                self.graph[pos] = value
                changed_pos.append(pos)
        return changed_pos
    def get_pos(self,target_value):
        poses = []
        for pos in self.graph:
            if self.graph[pos] == target_value:
                poses.append(pos)
        return poses
    def set_hollow(self,left_top:list[int,int],left_bottom:list[int,int],right_bottom:list[int,int],right_top:list[int,int],value):
        if not (left_top[0] == left_bottom[0] and left_bottom[1] == right_bottom[1] and right_bottom[0] == right_top[0] and right_top[1] == left_top[1]):
            raise Exception('parameter is not available')
        for i in range(left_bottom[1], left_top[1]+1):#왼쪽
            self.graph[left_top[0],i] = value
        for i in range(left_bottom[0],right_bottom[0]+1):#아래쪽
            self.graph[i,left_bottom[1]] = value
        for i in range(right_bottom[1],right_top[1]+1):#오른쪽
            self.graph[right_bottom[0],i] = value
        for i in range(left_top[0],right_top[0]+1):#위쪽
            self.graph[i,left_top[1]] = value
    def copy(self):
        result = Graph()
        result.graph = self.graph.copy()
        return result
def dijkstra(graph:Graph,start_pos:list[int,int],dest_pos:list[int,int],path_limit:int = math.inf):
    '''
    graph
        values except -1 and inf will be changed to inf
        -1 means wall that cannot go from current position'''
    inf = math.inf
    _graph = graph.copy()
    closest = []
    for p in graph:
        if not graph[p] in (-1, inf): graph[p] = inf
    class branch:
        def __init__(self,pos,distance,path:list):
            nonlocal closest, graph
            if len(closest) == path_limit:
                return
            if len(path) > graph[tuple(dest_pos)]:
                return
            if pos == dest_pos:
                if not closest:
                    closest = [path+[pos]]
                    return
                if distance + 1 < len(closest[0]):
                    closest = [path+[pos]]
                    return
                elif distance + 1 == len(closest[0]):
                    closest.append(path+[pos])
                    return
            x, y = pos[0], pos[1]
            

            if graph[x,y+1] != -1 and distance + 1 <= graph[x, y+1]:#위
                graph[x,y+1] = distance + 1
                _branch = branch([x,y+1],distance+1,path+[pos])
            

            if graph[x+1,y+1] != -1 and distance + 1 <=graph[x+1,y+1]:#오른쪽 위
                graph[x+1,y+1] = distance + 1
                _branch = branch([x+1,y+1],distance + 1,path+[pos])
            

            if graph[x+1,y] != -1 and distance + 1 <=graph[x+1,y]:#오른쪽
                graph[x+1,y] = distance + 1
                _branch = branch([x+1,y],distance+1,path+[pos])
            

            if graph[x+1,y-1] != -1 and distance + 1 <=graph[x+1,y-1]:#오른쪽 아래
                graph[x+1,y-1] = distance + 1
                _branch = branch([x+1,y-1],distance+1,path+[pos])
            

            if graph[x,y-1] != -1 and distance+1 <= graph[x,y-1]:#아래
                graph[x,y-1] = distance + 1
                _branch = branch([x,y-1],distance+1,path+[pos])
            

            if graph[x-1,y-1] != -1 and distance+1 <= graph[x-1,y-1]:#왼쪽 아래
                graph[x-1,y-1] = distance + 1
                _branch = branch([x-1,y-1],distance+1,path+[pos])
            

            if graph[x-1,y] != -1 and distance+1 <= graph[x-1,y]:#왼쪽
                graph[x-1,y] = distance + 1
                _branch = branch([x-1,y],distance+1,path+[pos])
            

            if graph[x-1,y+1] != -1 and distance + 1 <= graph[x-1,y+1]:#왼쪽 위
                graph[x-1,y+1] = distance + 1
                _branch = branch([x-1,y+1],distance+1,path+[pos])
    
            

    _branch = branch(start_pos,0,[])
    class route:
        def __init__(self,path:list,graph:Graph):
            self.path:list = path
            self.graph:Graph = graph
            self.path_graph:list[Graph] = []
            for p in path:
                __graph = graph.copy()
                for pos in __graph:
                    if not  __graph[pos] in (-1,inf): __graph[pos] = 0
                for pos in p:
                    __graph[tuple(pos)] = 1
                self.path_graph.append(__graph)

    result = route(closest,_graph)

    return result

if __name__ == '__main__':
    g = Graph()
    g.fill(math.inf)
    g.set_hollow([-1,11],[-1,-1],[11,-1],[11,11],-1)
    g.fill_area([3,7],[3,3],[7,3],[7,7],-1)
    print(g.graph)
    dijk = dijkstra(g,[0,0],[10,10])
    for i in dijk.path:
        print(i)
        print()