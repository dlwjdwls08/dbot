import math, random

Iterable = tuple,list

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

def difference(N:float,M:float):
    if N>M:
        return N - M
    elif N<M:
        return M - N
    else:
        return 0

def isprime(N:int):
    if N==1:
        return False
    for i in range(2, N):
        if not N % i:
            return False
    return True

def factorization(N:int):
    primes = []
    dummy = 0
    if isprime(N):
        return [(N,1)]
    for i in range(2,N):
        dummy = 0
        if N == 1:
            break
        if isprime(i) and not N % i:
            for o in range(1,int(N)):
                if not N % i**o:
                    dummy += 1
                else:
                    primes.append((i,dummy))
                    N /= i**dummy
                    break
    return primes

def divisor(N:int):
    result = []
    for i in range(1,N):
        if not N % i:
            result.append(i)
    return result

def common_divisor(*args:int):
    d = {}
    di = 0
    con = False
    result = []
    for i in args:
        d[di] = divisor(i)
        di += 1
    for o in divisor(args[0]):
        for n in d:
            if not o in d[n]:
                con = True
        if con:
            con = False
            continue
        result.append(o)
    return result

def least_common_multiple(*args:int):
    num = {}
    for i in args:
        for o in factorization(i):
            if not o[0] in num:
                num[o[0]] = 0
            if num[o[0]] < o[1]:
                num[o[0]] = o[1]
    result = 1
    for n in num:
        result *= n**num[n]
    return result

def greatest_common_factor(*args:int):
    num = {}
    con = False
    for i in args:
        for o in factorization(i):
            for a in args:
                if a % o[0]:
                    con = True
            if con:
                con = False
                continue
            if not o[0] in num:
                num[o[0]] = o[1]
            if num[o[0]] > o[1]:
                num[o[0]] = o[1]
    result = 1
    for n in num:
        result *= n**num[n]
    return result

def curve(*args:int, decimal_point:int=0):
    result = []
    for n,i in enumerate(args):
        if not n:
            continue
        if args[n-1] != i:
            different = True
            break
        different = False
    if not different:
        return [args[0]]
    for n, i in enumerate(args):
        if not n:
            continue
        past = args[n-1]
        if len(args) - 1 == n:
            if past > i:
                for i in range(abs(past - i) * 10**decimal_point + 1):
                    result.append(round(past - i/10**decimal_point,decimal_point))
            elif past < i:
                for i in range(abs(i - past) * 10**decimal_point + 1):
                    result.append(round(past + i/10**decimal_point,decimal_point))
        
        else:
            if past > i:
                for i in range(abs(past - i) * 10**decimal_point):
                    result.append(round(past - i/10**decimal_point,decimal_point))
            elif past < i:
                for i in range(abs(i - past) * 10**decimal_point):
                    result.append(round(past + i/10**decimal_point,decimal_point))
    return result

def array(start:int=0,end:int=0,decimal_point:int=0):
    result = []
    if start == end:
        return [start]
    if start > end:
        for i in range(abs(start - end) * 10**decimal_point + 1):
            result.append(round(start - i/10**decimal_point,decimal_point))
    elif start < end:
        for i in range(abs(end - start) * 10**decimal_point + 1):
            result.append(round(start + i/10**decimal_point,decimal_point))
    return result

def average(*args:float,decimal_point:int=0):
    result = 0
    for i in args:
        try:
            result += float(i)
        except:
            raise TypeError('function average gets integer of floating')
    return round(result/len(args),decimal_point)

def percentageof(reference_number:float,relative_number:float):
    return relative_number/reference_number

def distance(d1:tuple,d2:tuple):
    return math.sqrt(difference(d1[0], d2[0])**2 + difference(d1[1],d2[1])**2)

def randrange(start:float,stop:float,decimal_point:int=0):
    a = random.randrange(start * 10**decimal_point,stop * 10**decimal_point)
    return a / 10**decimal_point

def isiterable(variable):
    if type(variable) in (tuple,list,enumerate,range): return True
    else: return False

class Calculator:
    def __init__(self):
        self.resultlist = []
        self.resultdic = {}
    def add(self, ordinary, new=0):
        if isnum(ordinary) and isnum(new):
            result = rmzero(getnum(ordinary) + getnum(new))
            self.resultlist.append(result)
            print(self.resultlist)
            return result
        else: return ordinary