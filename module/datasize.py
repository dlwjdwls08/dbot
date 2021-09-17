import os, sys

unit = {'bit':8,'byte':1,'kb':-1,'mb':-2,'gb':-3,'tb':-4}

def sizeof(file,unitmode='byte'):
    if not unitmode in unit:
        raise Exception(f"unit doesn't exist in {unit}")
    return sys.getsizeof(file) * unit[unitmode] if unitmode in ('bit','byte') else 1024 ** unit[unitmode]