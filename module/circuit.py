

def OR(*bools:bool):
    if len(bools) == 1 and type(bools[0]) in (list,tuple):
        bools = bools[0]
    if True in bools: return True
    else: return False

def NOR(*bools:bool):
    if len(bools) == 1 and type(bools[0]) in (list,tuple):
        bools = bools[0]
    if True in bools: return False
    else: return True

def XOR(*bools:bool):
    if len(bools) == 1 and type(bools[0]) in (list,tuple):
        bools = bools[0]
    if True in bools and not bools.count(True) == len(bools): return True
    else: return False

def XNOR(*bools:bool):
    if len(bools) == 1 and type(bools[0]) in (list,tuple):
        bools = bools[0]
    if True in bools and not bools.count(True) == len(bools): return False
    else: return True

def AND(*bools:bool):
    if len(bools) == 1 and type(bools[0]) in (list,tuple):
        bools = bools[0]
    if bools.count(True) == len(bools): return True
    else: return False

def NAND(*bools:bool):
    if len(bools) == 1 and type(bools[0]) in (list,tuple):
        bools = bools[0]
    if bools.count(True) == len(bools): return False
    else: return True


if __name__ == '__main__':
    print(XOR())