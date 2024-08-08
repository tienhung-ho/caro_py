import time
from PIL import ImageTk, Image
from functools import partial
from tkinter import *
import tkinter as tk

import PIL.Image
from PIL import *
from Player import *


class Player:
    def __init__(self):
        self.image_List = {}
        self.status_Player = {}
        self.text_List = {}
        self.color_List = {}
        self.player_Name = {}
        self.tiso_player = {}
        self.text_List[0] = 'X'
        self.status_Player[0] = 0
        self.color_List[0] = 'red'
        self.player_Name[0] = 'Player-1'
        self.tiso_player[0] = 0
        self.text_List[1] = 'O'
        self.status_Player[1] = 1
        self.color_List[1] = 'blue'
        self.player_Name[1] = 'Player-2'
        self.tiso_player[1] = 0


class Screen(tk.Tk):

    def __init__(self):
        super().__init__()
        self.memory = []
        self.button_List = {}
        self.status_List = {}
        self.flag = True
        self.player = Player()
        # self.my_Canvas = Canvas(self, width=1080, height=608)
        try:
            self.title("Caro")
            self.iconbitmap('D:\Caro\images\icon.ico')
        except:
            pass
        self.Ox = 17
        self.Oy = 35
        self.stack = list()
        self.tiso = [0] * 2



        # self.frame_Body = Frame(self)
        # self.frame_Body.pack()


    def click(self, x=1, y=1):

        # self.player.img_Player()
        if not self.status_List[x, y]:
            if self.flag:
                self.button_List[x, y]['text'] = self.player.text_List[0]
                self.button_List[x, y]['foreground'] = self.player.color_List[0]
                self.flag = False
                self.status_List[x, y] = True
                self.stack.append([x, y])
                if self.check(x, y, coor='X', Ox=17, Oy=35):
                    self.mess_box(self.Ox, self.Oy, self.player.status_Player[0])
                    self.stop()
                    self.tiso[0] += 1
                    # self.status_List[x, y] = True
                # self.button_List[x, y]['image'] = self.player.image_List

            else:
                self.button_List[x, y]['text'] = self.player.text_List[1]
                self.button_List[x, y]['foreground'] = self.player.color_List[1]
                self.flag = True
                self.status_List[x, y] = True
                self.stack.append([x, y])
                if self.check(x, y, coor='O', Ox=17, Oy=35):
                    self.mess_box(self.Ox, self.Oy, self.player.status_Player[1])
                    self.tiso[1] += 1
                    self.stop()

    def menu_main(self, Ox, Oy):
        bg = ImageTk.PhotoImage(file="D:\Caro\images\jungle2.jpg")
        self.Ox = Ox
        self.Oy = Oy
        # Create a Canvas
        self.my_Canvas = Canvas(self, width=1080, height=605)
        self.my_Canvas.pack(fill=BOTH, expand=True)

        # Add Image inside the Canvas
        self.my_Canvas.create_image(0, 0, image=bg, anchor='nw')
        #Add button
        bt_play = Button(self, text='Play', font=('Matura MT Script Capitals', 10),
                         borderwidth=5, anchor='center', width=14, height=2, command=partial(self.dislay, Ox, Oy))
        bt_op = Button(self, text='Option', font=('Matura MT Script Capitals', 10),
                       borderwidth=5, anchor='center', width=14, height=2, command=partial(self.option_Menu, Ox, Oy))
        bt_ex = Button(self, text='Exit', font=('Matura MT Script Capitals', 10),
                       borderwidth=5, anchor='center', width=14, height=2, command=self.quit)
        # bt_Win = self.my_Canvas.create_window(0, 0, window=bt_play)
        global image, resized, image2
        # open image to resize it
        image = PIL.Image.open("D:\Caro\images\jungle2.jpg")
        # resize the image with width and height of root
        resized = image.resize((1080, 605))
        image2 = ImageTk.PhotoImage(resized)
        self.my_Canvas.create_image(0, 0, image=image2, anchor='nw')
        # geometry
        self.my_Canvas.create_window(1080 // 2, 605 // 2 + 60, window=bt_play)
        self.my_Canvas.create_window(1080 // 2, 605 // 2 + 115, window=bt_op)
        self.my_Canvas.create_window(1080 // 2, 605 // 2 + 170, window=bt_ex)

        # add text
        self.my_Canvas.create_text(1080 // 2 - 10, 605 // 2 - 100, text="Caro",
                                   font=('Matura MT Script Capitals', 150), fill='White')

    def back_menu(self, Ox, Oy):
        self.my_Canvas.destroy()
        self.menu_main(Ox, Oy)

    def option_Menu(self, Ox, Oy):
        self.my_Canvas.destroy()
        bg = ImageTk.PhotoImage(file="D:\Caro\images\jungle2.jpg")

        # Create a Canvas
        self.my_Canvas = Canvas(self, width=1080, height=605)
        self.my_Canvas.pack(fill=BOTH, expand=True)

        # Add Image inside the Canvas
        self.my_Canvas.create_image(0, 0, image=bg, anchor='nw')
        # Add entry
        bt_player1 = Button(self, text='Player 1', borderwidth=3, height=1,
                            width=15, font=('Harlow Solid Italic', 20), bg='grey',
                            command=self.pl_define1)
        bt_player2 = Button(self, text='Player 2', borderwidth=3, height=1,
                            width=15, font=('Harlow Solid Italic', 20), bg='grey',
                            command=self.pl_define2)
        bt_time5 = Button(self, text='5 minute', borderwidth=3, height=1,
                          width=15, font=('Harlow Solid Italic', 20), bg='grey',
                          command=partial(self.minute, 5))
        bt_time10 = Button(self, text='10 minute', borderwidth=3, height=1,
                           width=15, font=('Harlow Solid Italic', 20), bg='grey',
                           command=partial(self.minute, 10))
        bt_time15 = Button(self, text='15 minute', borderwidth=3, height=1,
                           width=30, font=('Harlow Solid Italic', 20), bg='grey',
                           command=partial(self.minute, 15))
        bt_back = Button(self, text='Back', borderwidth=3, height=1,
                         width=30, font=('Harlow Solid Italic', 20), bg='grey',
                         command=partial(self.back_menu, Ox, Oy))

        # bt_Win = self.my_Canvas.create_window(0, 0, window=bt_play)
        global image, resized, image2
        # open image to resize it

        image = PIL.Image.open("D:\Caro\images\jungle2.jpg")
        # resize the image with width and height of root
        resized = image.resize((1080, 605))
        image2 = ImageTk.PhotoImage(resized)

        self.my_Canvas.create_image(0, 0, image=image2, anchor='nw')
        # add entry

        # add button
        self.my_Canvas.create_window(400, 260, window=bt_player1)
        self.my_Canvas.create_window(400, 340, window=bt_player2)
        self.my_Canvas.create_window(400 + 300, 260, window=bt_time5)
        self.my_Canvas.create_window(400 + 300, 340, window=bt_time10)
        self.my_Canvas.create_window(400 + 150, 420, window=bt_time15)
        self.my_Canvas.create_window(400 + 150, 500, window=bt_back)
        # add text
        self.my_Canvas.create_text(1080 // 2 - 10, 605 // 2 - 200,
                                   text="Option", font=('Matura MT Script Capitals', 50),fill='grey')

    def menu_bar(self, Ox, Oy):
        my_menu = Menu(self)
        self.config(menu=my_menu)
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New...', command=partial(self.newgame))
        file_menu.add_command(label='Exit', command=self.quit)

    def minute(self, mn1):
        return mn1 -1
    # add back button

    def dislay(self, Ox=10, Oy=10):
        self.my_Canvas.destroy()
        self.menu_bar(Ox, Oy)
        frame_Menu = Frame(self)
        frame_Menu.pack()
        frame_Body = Frame(self)
        frame_Body.pack()
        a, b = self.tiso[0], self.tiso[1]
        # add button, label, entry

        my_button = Button(frame_Menu, width=6, borderwidth=2, text='Undo', font=('arial', 12, 'bold'), command=self.stack_undo)
        my_button.grid(row=1, column=0)
        # # my_Label0 = Label(frame_Menu, borderwidth=3, height=2, width=3, font=('arial', 12, 'bold'),
        # #                   text=f'{a}')
        # my_Label0.grid(row=1, column=2)
        my_Label1 = Label(frame_Menu,  height=2, width=18, font=('arial', 12, 'bold'),
                          foreground=f'{self.player.color_List[0]}', text=f'{self.player.player_Name[0]}')

        my_Label1.grid(row=1, column=3)
        my_Label2 = Label(frame_Menu, height=2, width=18, font=('arial', 12, 'bold'),
                          foreground=f'{self.player.color_List[1]}', text=f'{self.player.player_Name[1]}')
        my_Label2.grid(row=1, column=4)
        # my_Label3 = Label(frame_Menu, borderwidth=3, height=2, width=3, font=('arial', 12, 'bold'),
        #                   text=f'{self.tiso[1]}')
        # my_Label3.grid(row=1, column=6)



        for x in range(Ox):
            for y in range(Oy):
                self.button_List[x, y] = tk.Button(frame_Body, height=1, width=2, foreground='red',
                                                   borderwidth=3, image='', text='', font=('arial', 15, 'bold')
                                                   , relief=tk.RIDGE, command=partial(self.click, x=x, y=y))
                self.button_List[x, y].grid(row=x, column=y)
                self.status_List[x, y] = False


    def stop(self):
        for x in range(self.Ox):
            for y in range(self.Oy):
                # self.button_List[x, y]['text'] = ''
                self.status_List[x, y] = True

    def newgame(self):
        for x in range(self.Ox):
            for y in range(self.Oy):
                self.button_List[x, y]['text'] = ''
                self.status_List[x, y] = False

    def check(self, x, y, coor, Ox, Oy):

        #hang ngang

        i, j = x, y
        count = 0

        while i > 0 and self.button_List[i, j]['text'] == coor:
            count += 1
            i -= 1

        i = x
        while i < Ox and self.button_List[i, j]['text'] == coor:
            count += 1
            i += 1

        if count >= 6:
            return True

        #hang doc
        i, j = x, y
        count = 0

        while j > 0 and self.button_List[i, j]['text'] == coor:
            count += 1
            j -= 1

        j = y
        while j < Oy and self.button_List[i, j]['text'] == coor:
            count += 1
            j += 1

        if count >= 6:
            return True

        i, j = x, y
        count = 0

        #cheo trai
        while i > 0 and j < Oy and self.button_List[i, j]['text'] == coor:
            count += 1
            i -= 1
            j -= 1

        i, j = x, y

        while i < Ox and j > 0 and self.button_List[i, j]['text'] == coor:
            count += 1
            i += 1
            j += 1

        if count >= 6:
            return True

        #cheo phai
        i, j = x, y
        count = 0

        while i > 0 and j > 0 and self.button_List[i, j]['text'] == coor:
            count += 1
            i -= 1
            j += 1

        i, j = x, y
        while i < Ox and j < Oy and self.button_List[i, j]['text'] == coor:
            count += 1
            i += 1
            j -= 1

        if count >= 6:
            return True

    def pl_define1(self):

        top = Toplevel()
        top.title("Caro")
        top.iconbitmap('D:\Caro\images\icon.ico')

        win_width, win_height = 200, 200
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_axis = int((screen_width / 2) - (win_width / 2))
        y_axis = int((screen_height / 2) - (win_height / 2))
        top.geometry(f'{win_width}x{win_height}+{x_axis}+{y_axis}')

        # add entry, label, button
        lb_name = Label(top, text='Enter your name:', font=('Calibri', 20))
        et_name = Entry(top, width=30)
        lb_color = Label(top, text='Enter your color:', height=2, font=('Calibri', 20))
        et_color = Entry(top, width=30)

        def vl_get():
            valname = et_name.get()
            valcolor = et_color.get()
            self.player.color_List[0] = f'{valcolor}'
            self.player.player_Name[0] = f'{valname}' + '(P1)'
            self.player.status_Player[0] = 0

        bt_submit = Button(top, text='Submit',
                           width=15, height=1, borderwidth=3, command=lambda: [vl_get(), top.destroy()])

        # dislay
        lb_name.grid()
        et_name.grid()
        lb_color.grid()
        et_color.grid()
        bt_submit.grid()

    def pl_define2(self):

        top1 = Toplevel()
        top1.title("Caro")
        top1.iconbitmap('D:\Caro\images\icon.ico')

        win_width, win_height = 200, 200
        screen_width = top1.winfo_screenwidth()
        screen_height = top1.winfo_screenheight()
        x_axis = int((screen_width / 2) - (win_width / 2))
        y_axis = int((screen_height / 2) - (win_height / 2))
        top1.geometry(f'{win_width}x{win_height}+{x_axis}+{y_axis}')

        # add entry, label, button
        lb_name = Label(top1, text='Enter your name:', font=('Calibri', 20))
        et_name = Entry(top1, width=30)
        lb_color = Label(top1, text='Enter your color:', height=2, font=('Calibri', 20))
        et_color = Entry(top1, width=30)

        # use value
        def vl_get():
            valname = et_name.get()
            valcolor = et_color.get()
            self.player.color_List[1] = f'{valcolor}'
            self.player.player_Name[1] = f'{valname}' + '(P2)'
            self.player.status_Player[1] = 1

        bt_submit = Button(top1, text='Submit',
                           width=15, height=1, borderwidth=3, command=lambda: [vl_get(), top1.destroy()])

        # dislay
        lb_name.grid()
        et_name.grid()
        lb_color.grid()
        et_color.grid()
        bt_submit.grid()

    def mess_box(self, Ox, Oy, status):

        # create
        box = Toplevel()
        box.title("Caro")
        box.iconbitmap('D:\Caro\images\icon.ico')

        # resize 1
        global image1, resized1, pic1

        # open image to resize it
        image1 = PIL.Image.open("D:\Caro\images\player1-win.png")
        # resize the image with width and height of root
        resized1 = image1.resize((600, 500))
        pic1 = ImageTk.PhotoImage(resized1)

        #resize 2
        global image2, resized2, pic2
        # open image to resize it
        image2 = PIL.Image.open("D:\Caro\images\player2-win.jpg")
        # resize the image with width and height of root
        resized2 = image2.resize((600, 500))
        pic2 = ImageTk.PhotoImage(resized2)

        # dislay
        if status == 0:
            lb_mess1 = Label(box, image=pic1)
            bt_mess1 = Button(box, borderwidth=3, text='New game!', anchor='s',
                              command=lambda: [(self.newgame(), box.destroy())])
            lb_mess1.grid()
            bt_mess1.grid()
        else:
            lb_mess2 = Label(box, image=pic2)
            bt_mess2 = Button(box, borderwidth=3, text='New game!', anchor='s',
                              command=lambda: [(self.newgame(), box.destroy())])
            lb_mess2.grid()
            bt_mess2.grid()

    def stack_undo(self):
        stack_axit = list()
        stack_axit = self.stack.pop()
        x, y = stack_axit[0], stack_axit[1]
        if x and y:
            self.status_List[x, y] = False
            self.button_List[x, y]['text'] = ''
        stack_axit = list()


if __name__ == "__main__":
    # Screen push
    splash_root = Tk()
    splash_root.title("Caro")
    splash_root.iconbitmap('D:\Caro\images\icon.ico')


    # images

    img = PIL.Image.open('D:\Caro\images\push.png')
    rz = img.resize((720, 405))
    pic_img = ImageTk.PhotoImage(rz)
    splash_Label = Label(splash_root, image=pic_img)

    # push

    win_width, win_height = 720, 405
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()
    x_axis = int((screen_width / 2 ) - (win_width / 2))
    y_axis = int((screen_height / 2) - (win_height / 2))

    # hide the border

    splash_root.geometry(f'{win_width}x{win_height}+{x_axis}+{y_axis}')
    splash_root.overrideredirect(True)
    splash_Label.pack()

    def screen_main():
        splash_root.destroy()

        new = Screen()
        new.menu_main(17, 35)


    splash_root.after(4000, screen_main)

    mainloop()

