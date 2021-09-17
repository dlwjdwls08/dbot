import pygame, math

from pygame import event
from pygame import display
from pygame.constants import MOUSEBUTTONUP, MOUSEMOTION


# def isclicked(objpos,cir=False,tri=False,radious=0):
#     mousepos = pygame.mouse.get_pos()
#     if cir:
#         distance = math.sqrt(cal.sub(objpos[0],mousepos[0])**2 + cal.sub(mousepos[1], objpos[1])**2)
#         for e in pygame.event.get():
#             if e.type == pygame.MOUSEBUTTONDOWN and distance <= radious:
#                 return True
#     elif tri:
#         pass
#     else:

#     return False
screen = display.set_mode((100,100))



def eventdetect():
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()


#condition = 조건, func_and_args = (함수, 매개변수) 또는 (이름, 불린값), returncondition = or,and,nor,nand,xor,nxor 중 하나
def eventcheck(eventget:pygame.event.get, condition:list[object], *func_and_args:list[str,bool]):
    condition = [str(i) for i in condition]
    boolreturn = {}
    for i in func_and_args:    #불린값 딕셔너리 생성
        if len(i) == 1:
            continue
        if type(i[1]) == bool:
            boolreturn[i[0]] = False
    for e in eventget:    #이벤트를 대입
        etype = str(e.type)
        if etype == str(pygame.KEYDOWN):    #이벤트에 키 입력이 있는경우
            ekey = str(e.key)
            if ekey in condition:    #입력키가 조건에 있는경우
                if len(func_and_args[condition.index(ekey)]) == 1:    #매개변수가 없는 경우
                    func_and_args[condition.index(ekey)][0]()
                elif type(func_and_args[condition.index(ekey)][1]) == bool:    #변환값이 불린일 경우
                    boolreturn[func_and_args[condition.index(ekey)][0]] = func_and_args[condition.index(ekey)][1]
                elif len(func_and_args[condition.index(ekey)]) == 2:    #일반적인 경우
                    func_and_args[condition.index(ekey)][0](func_and_args[condition.index(ekey)][1])

                else:    #매개변수가 없을 경우
                    func_and_args[condition.index(etype)][0]()
        
        if etype in condition:    #이벤트에 조건이 있는경우
            if len(func_and_args[condition.index(etype)]) == 1:    #매개변수가 없는 경우
                func_and_args[condition.index(etype)][0]()
            elif type(func_and_args[condition.index(etype)][1]) == bool:    #변환값이 불린일 경우
                boolreturn[func_and_args[condition.index(etype)][0]] = func_and_args[condition.index(etype)][1]
            elif len(func_and_args[condition.index(etype)]) == 2:    #일반적인 경우
                func_and_args[condition.index(etype)][0](func_and_args[condition.index(etype)][1])

    return boolreturn

# if __name__=='__main__':
#     while True:
#         mmotion = MOUSEMOTION
#         eventcheck(event.get(), [pygame.MOUSEBUTTONDOWN,pygame.QUIT,pygame.K_c], [print,'a'],[quit],[print,'b'])