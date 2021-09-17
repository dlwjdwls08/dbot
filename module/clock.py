import time, datetime, threading, winsound, asyncio, functools
from typing import Literal, overload

def isnum(N):
    try:
        float(N)
        return True
    except:
        return False

def getnum(N):
    try:
        float(N)
        return float(N)
    except:
        raise Exception('argument is string')

def rmzero(s):
    if isnum(s):
        result = '%g' % getnum(s)
        if result.count('.') == 1:
            return float(result)
        else:
            return int(result)
    else: return s




class StopWatch:
    def init(self):
        self.time:dict[Literal['start','stop','pause','unpause']] = {'start':0,'stop':0,'pause':0,'unpause':0}
        self.values:dict[Literal['start','pause']] = {'start':False,'pause':False}
        self.name = ''

    def __init__(self) -> None:
        self.records:dict[Literal['record\'s name']] = {}
        self.init()
    
    def start(self,name:Literal['0, 1, 2, ...'] = None):
        if self.values['start']: raise Exception('already started')
        self.time['start'] = time.time()
        self.values['start'] = True
        if name:
            self.name = name
        else:
            n = 0
            while True:
                if not n in self.records:
                    self.name = n
                    break
                n += 1

    def stop(self):
        if not self.values['start']: raise Exception('haven\'t been started')
        self.time['stop'] = time.time()
        self.values['start'] = False
        v = self.time['stop'] - self.time['start']
        if self.values['pause']: v -= (self.time['stop'] - self.time['pause'])
        day = v//(3600*24)
        v -= day*3600*24
        hour = v//3600
        v -= hour*3600
        minute = v//60
        v -= minute*60
        second = v//1
        v -= second
        millisecond = v
        result = {'day':day,'hour':hour,'minute':minute,'second':second,'millisecond':millisecond}
        self.records[self.name] = result
        self.values['pause'] = False

    def pause(self):
        if self.values['pause']: raise Exception('already paused')
        self.time['pause'] = time.time()
        self.values['pause'] = True

    def unpause(self):
        if not self.values['pause']: raise Exception('haven\'t been paused')
        self.time['unpause'] = time.time()
        self.values['pause'] = False
        self.time['start'] += self.time['unpause'] - self.time['pause']

    def get_now(self) -> dict[Literal['day','hour','minute','second','millisecond']]:
        if not self.time['start']: raise Exception("haven't been started or already stopped")
        now = time.time()
        v = now - self.time['start']
        if self.values['pause']: v -= (now - self.time['pause'])
        day = v//(3600*24)
        v -= day*3600*24
        hour = v//3600
        v -= hour*3600
        minute = v//60
        v -= minute*60
        second = v//1
        v -= second
        millisecond = v*10000
        return {'day':day,'hour':hour,'minute':minute,'second':second,'millisecond':millisecond}

    def get_result(self,name:Literal["record's name"] = None):
        if name == None:
            if len(self.records.values()) == 0: raise Exception("there's no record")
            return list(self.records.values())[0]
        if not name in self.records: raise Exception("record having that name doesn't exist")
        return self.records[name]

class Timer:
    def __init__(self) -> None:
        self.timers:dict = {}
    class _Timer:
        def __init__(self,finish = None,do_finish:bool = False) -> None:
            self.time:dict[Literal['start','stop','pause','unpause']] = {'start':0,'stop':0,'pause':0,'unpause':0}
            self.values:dict[Literal['start','pause']] = {'start':False,'pause':False}
            self.result = None
            self.finish = finish
            self.do_finish = do_finish


        def start(self,second):
            if self.values['start']: raise Exception('already started')
            now = time.time()
            self.time['start'] = now
            self.time['stop'] = now + second
            self.values['start'] = True
            def t_():
                while True:
                    if time.time() >= self.time['stop'] and not self.values['pause']:
                        if self.do_finish:
                            self.result = self.finish()
                        else:
                            self.result = self.finish
                        break
                    if not self.values['start']:
                        break
            
            t = threading.Thread(target=t_,daemon=True)
            t.start()
        
        def stop(self):
            if not self.values['start']: raise Exception('haven\'t been started')
            self.values['start'] = False
            self.values['pause'] = False

        def pause(self):
            if self.values['pause']: raise Exception('already paused')
            self.values['pause'] = True
            now = time.time()
            self.time['pause'] = now
            

        def unpause(self):
            if not self.values['pause']: raise Exception("haven't been paused")
            self.values['pause'] = False
            now = time.time()
            self.time['unpause'] = now
            self.time['stop'] += self.time['unpause'] - self.time['pause']

        def get_now_left(self):
            if not self.values['start']: raise Exception("haven't started or already stopped")
            now = time.time()
            v = self.time['stop'] - now
            day = v//(3600*24)
            v -= day*3600*24
            hour = v//3600
            v -= hour*3600
            minute = v//60
            v -= minute*60
            second = v//1
            v -= second
            millisecond = v*10000
            return {'day':day,'hour':hour,'minute':minute,'second':second,'millisecond':millisecond}
            
        def get_now_wasted(self):
            if not self.values['start']: raise Exception("haven't started or already stopped")
            now = time.time()
            v = now - self.time['start']
            if self.values['pause']: v -= (now - self.time['pause'])
            day = v//(3600*24)
            v -= day*3600*24
            hour = v//3600
            v -= hour*3600
            minute = v//60
            v -= minute*60
            second = v//1
            v -= second
            millisecond = v*10000
            return {'day':day,'hour':hour,'minute':minute,'second':second,'millisecond':millisecond}
    @overload
    def add_timer(self,name:str,time:float): ...
    @overload
    def add_timer(self,name:str,time:float,finish_func,do_finish_func:bool = False): ...
    def add_timer(self,*args,**kwargs):...

class Clock(StopWatch):
    pass



if __name__ == '__main__':
    # tm = Timer()
    # tm.start(5,functools.partial(print,'a'),True)
    # time.sleep(10)
    print(Timer.add_timer.__annotations__)