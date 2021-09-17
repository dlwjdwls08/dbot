import random
from types import FunctionType, GenericAlias
import types, typing

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

symbols = [')','!','@','#','$','%','^','&','*','(']

def randrange_decimal(start, stop, decimal_point=0) -> float:
    a = random.randrange(start * 10**decimal_point, stop * 10**decimal_point + 1)
    return a / 10**decimal_point

def args_to_hints(func:FunctionType,*args) -> list:
    args = list(args)
    types = list(func.__annotations__.values())
    _args = []
    for n, arg in enumerate(args):
        try:
            arg = types[n](arg)
        except:
            pass
        _args.append(arg)
    return _args

def list_to_str(List:list[str or int], blank=True) -> str:
    result = ''
    for n, content in enumerate(List):
        result += str(content) 
        result += ',' if n + 1 != len(List) else ''
        result += ' ' if n + 1 != len(List) and blank else ''
    return result

def list_to_original(List:list[str or int]) -> str:
    result = ''
    for i in List:
        result += i + ' '
    return result.strip()

def type_available(object,type_) -> bool:
    try:
        type_(object)
        return True
    except:
        return False



class Graph:
    '''
    Create a graph\n
    ex
    ```
    g = Graph()
    g[1,4] = True
    print(g[1,4])
    >>> True
    print(g[3,5])
    >>> None
    print(g.graph)
    >>> {(1, 4): True, (3, 5): None}
    ```'''
    _postype = list[float,float] or tuple[float,float]

    def __init__(self,graph:dict = None, default_value:typing.Any = None):
        if not type(graph) == dict: raise Exception("Invalid form of graph : graph")
        self.graph = {} if not graph else graph
        self.default_value = default_value
    def __getitem__(self,pos):
        if not self._ispos(pos): raise Exception("Invalid form of pos")
        if not pos in self.graph:
            self.graph[pos] = self.default_value
        return self.graph[pos]
    def __setitem__(self,pos,value):
        if not self._ispos(pos): raise Exception("Invalid form of pos")
        self.graph[pos] = value
        return value
    def __delitem__(self,pos):
        if not self._ispos(pos): raise Exception("Invalid form of pos")
        if pos in self.graph:
            del self[pos]
    def __iter__(self):
        return iter(self.graph)
    def __add__(self,graph):
        _graph = self.copy()
        graph:Graph
        for pos in graph:
            if not _graph[pos]:
                _graph[pos] = graph[pos]
        return _graph
    def _ispos(self,obj:list or tuple):
        if not type(obj) in (list, tuple): return False
        if len(obj) != 2: return False
        if (not type(obj[0]) in (int,float)) or (not type(obj[1]) in (int,float)): return False
        return True
    def copy(self):
        _graph = Graph()
        _graph.__dict__ = self.__dict__
        return _graph
    def render(self,left_bottom,right_top:list[int,int]):
        if not self._ispos(left_bottom): raise Exception("Invalid form of pos : left_bottom")
        if not self._ispos(right_top): raise Exception("Invalid form of pos : right_top")
        for i in range(left_bottom[0],right_top[0]+1):
            for j in range(left_bottom[1],right_top[1]+1):
                self.graph[i,j] = self.default_value
    def clear(self):
        self.graph = {}
        
if __name__ == '__main__':
    g = Graph()
    g[1,1] = True
    h = Graph()
    h[2,2] = False
    # print(g.copy())
    t = g + h
    print(t.graph)
    