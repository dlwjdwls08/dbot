import tkinter, functools
from tkinter import ttk
def choice(*options:str or list[str], multi_choose:bool = False, already_chosen:bool = False, GUI_name = 'Choice Screen') -> list or None:
    win = tkinter.Tk()
    win.wm_title(GUI_name)
    if len(options) == 1 and type(options[0]) == list:
        options = options[0]
    
    if multi_choose:
        result = []
        def button(value):
            nonlocal result
            if value in result:
                result.remove(value)
            else:
                result.append(value)
            if result:
                confirm['state'] = tkinter.NORMAL
            else:
                confirm['state'] = tkinter.DISABLED
            if already_chosen: confirm['state'] = tkinter.NORMAL
        for n, option in enumerate(options):
            col = n % 4 + 1
            text = option
            if len(option) > 6:
                text = option[0:7]+'...'
            Cb = tkinter.Checkbutton(win,text=text,command=functools.partial(button,option))
            Cb.grid(column=col,row=n//4)
            if already_chosen:
                Cb.select()
        def ret():
            win.destroy()
            return result
        confirm = ttk.Button(win,text='Confirm',command=ret)
        confirm['state'] = tkinter.NORMAL if already_chosen else tkinter.DISABLED
        confirm.grid(column=(n+1)%4 + 1, row=n//4+1)
        for i in options:
            result.append(i)
        win.mainloop()
        return result
    else:
        result = tkinter.StringVar(win,value=None)
        def button():
            confirm['state'] = tkinter.NORMAL
        for n, option in enumerate(options):
            col = n % 4 + 1
            text = option
            if len(option) > 6:
                text = option[0:7]+'...'
            tkinter.Radiobutton(win,text=text,variable=result,value=option,command=button).grid(column=col,row=n//4)
        def ret():
            win.destroy()
            return result.get()
        confirm = ttk.Button(win,text='Confirm',command=ret)
        confirm['state'] = tkinter.DISABLED
        confirm.grid(column=(n+1)%4 + 1, row=n//4+1)
        win.mainloop()
        return result.get()
if __name__ == '__main__':
    print((choice('hi','bye','a','b','c','d','adsfjklsadkfjklasdfkj',multi_choose=True,already_chosen=True)))