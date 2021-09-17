import re, types, typing, inspect
from typing_extensions import Literal
from module import useful

class RGB:
    RED = 255,0,0
    GREEN = 0,255,0
    BLUE = 0,0,255
    MAGENTA = 255,0,255
    YELLOW = 255,255,0
    CYAN = 0,255,255
    WHITE = 255,255,255
    BLACK = 0,0,0
    GRAY = 128,128,128

class Hexadecimal:
    RED = 0xFF0000
    GREEN = 0x00FF00
    BLUE = 0x0000FF
    MAGENTA = 0xFF00FF
    YELLOW = 0xFFFF00
    CYAN = 0x00FFFF
    WHITE = 0xFFFFFF
    BLACK = 0x000000

def hex_to_rgb(hex_:Literal['0x[a-f0-9]{6}']):
    p = re.compile('0x[a-f0-9]{6}')
    if not p.fullmatch(hex_):
        raise Exception("hex parameter isn't hex type")
    h = hex_.split('x')[1]
    r = h[0:2]
    g = h[2:4]
    b = h[4:6]
    rgb = [] 
    l:list = [str(i) for i in range(10)] + useful.alphabet[0:6]
    for c in [r,g,b]:
        rgb.append(l.index(c[0])*16 + l.index(c[1]))  
    return rgb

def rgb_to_hex(rgb:list[int,int,int]):
    e = Exception("rgb parameter isn't right form")
    if not (type(rgb) == list and len(rgb) == 3):
        raise e
    for c in rgb:
        if type(c) != int:
            raise e
    l:list = [str(i) for i in range(10)] + useful.alphabet[0:6]
    r = l[rgb[0]//16] + l[rgb[0]%16]
    g = l[rgb[1]//16] + l[rgb[1]%16]
    b = l[rgb[2]//16] + l[rgb[2]%16]
    return f'0x{r}{g}{b}'

