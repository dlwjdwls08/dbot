import inspect
from typing import overload
import typing

funcs = {}


class Overload:
    def overload(func):
        '''Overload
        
        available using different method of which name is same
        (but many bugs and restrictions)
        ```
        @typing.overload #you should not do this, but you can various parameter hints with VSC if you do this
        @Overload.overload
        def test_func(args,kwargs):
            <Implements>
        
        @typing.overload
        @Overload.overload
        def test_func(args1,arg2,kwargs):
            <Implements>
        ...
        
        def test_func(*args,**kwargs):
            Overload.overload_pass(test_func,args,kwargs)

        
        '''
        overload(func)
        if not func.__name__ in funcs:
            funcs[func.__name__] = []
        funcs[func.__name__].append(func)
        if inspect.getargs(func).varargs: raise ValueError('method that is decorated by overload can\'t contain `*args` parameter')
        def wrapper(*args,**kwargs):
            func(*args,**kwargs)
        return wrapper
    def overload_pass(self,args,kwargs):
        # print(inspect.getargs(self.__code__),inspect.signature(self).parameters)
        args = list(args)
        kwargs = dict(kwargs)
        
        for f in funcs[self.__name__]:
            fsig = inspect.signature(f)
            
        
        for f in funcs[self.__name__]:
            fargs = inspect.getargs(f.__code__)
            # print(inspect.getargs(f.__code__).args,'   ,   ',args,'   ,   ',kwargs)
            # print(fargs.args,fargs.varargs,fargs.varkw)
            no = False
            print(inspect.signature(f).parameters)
            print(fargs,fargs.args,fargs.varkw,args,kwargs)
            _args = []
            _kwargs = kwargs.copy()
            for k in kwargs:
                if fargs.args:
                    if not k in fargs.args:
                        if fargs.varkw:
                            if not k in fargs.varkw:
                                no = True
                                break
                        else:
                            no = True
                            break
                if k in fargs.args:
                    _args.insert(fargs.args.index(k),_kwargs.pop(k))
            
            
            fa = fargs.args
            fk = fargs.varkw
            if not fa: fa = []
            if not fk: fk = {}
            if not no and len(fa) == len(args+_args):
                
                f(*args+_args,**_kwargs)

            

@typing.overload
@Overload.overload
def a(a:int,b:int):
    print(a,b)
@typing.overload
@Overload.overload
def a(a,b,c):
    print(a,b,c)
@typing.overload
@Overload.overload
def a(a,*d):
    print(a,d)
@typing.overload
@Overload.overload
def a(a,b = 1,d=3):
    print(a,b,d)
@typing.overload
@Overload.overload
def a(**kwargs):
    print(kwargs)
def a(*args,**kwargs):
    Overload.overload_pass(a,args,kwargs)

a(s='hm',y='y')

a('hi','bye','rehi','rebye')