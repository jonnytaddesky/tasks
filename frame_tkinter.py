from tkinter import *


tk = Tk()
tk.title('Hello, World!')

frame = Frame(tk, borderwidth=2)

tk.eval('tk::PlaceWindow . center')

frame.pack(fill=BOTH, expand=1)

label = Label(frame, text='Hello, World!')
label.pack(fill=X, expand=1)


def say_hi():
    print('Всем привет!')


hi_there = Button(frame)
hi_there['text'] = 'click me'
hi_there['command'] = say_hi
hi_there.pack(side='top')

quit = Button(frame, text='QUIT', fg='RED', command=tk.destroy)
quit.pack(side='bottom')
tk.mainloop()
