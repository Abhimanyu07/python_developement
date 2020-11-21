#RGB TO HEX
from tkinter import *
from functools import partial

#function which actually does so
def rgb_to_hex(labelres, r1, g1, b1):
    hex_ = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while 1:
        hex_code = "#"
        try:
            r_ = int(r1.get())
            g_ = int(g1.get())
            b_ = int(b1.get())
            in_color = [r_, g_, b_]
            if -1 < r_ < 256 and -1 < g_ < 256 and -1 < b_ < 256:
                for j in in_color:
                    f = (j // 16)
                    if f >= 10:
                        f = hex_[f]
                    f = str(f)
                    s = (j % 16)
                    if s >= 10:
                        s = hex_[s]
                    s = str(s)
                    hex_code += f + s
                labelres.config(text=hex_code)
                gui.config(bg=hex_code) #updates the background with the hexcode you calculated 
                return
            else:
                raise ValueError
        except ValueError:
            print("invalid values")
            labelres.config(text="Error")
            return

#gui stuff 
#There will be some formatting 
gui = Tk()
gui.config(bg='light green')
gui.title('RGB To HEXCODE')
gui.geometry('300x600')
l_red = Label(gui, text="  RED  ").grid(row=2, column=0)
l_green = Label(gui, text="GREEN").grid(row=6, column=0)
l_blue = Label(gui, text=" BLUE ").grid(row=10, column=0)
r = StringVar()
g = StringVar()
b = StringVar()
red = Entry(gui, textvariable=r).grid(row=2, column=2)
green = Entry(gui, textvariable=g).grid(row=6, column=2)
blue = Entry(gui, textvariable=b).grid(row=10, column=2)
label_result = Label(gui)
label_result.grid(row=14, column=2)
rgb_to_hex = partial(rgb_to_hex, label_result, r, g, b)
button_to_hex = Button(gui, text='Convert', command= rgb_to_hex).grid(row=14,column=0)
gui.mainloop()
