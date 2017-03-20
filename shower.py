import tkinter as tk

BLANK_H = 150 #棋盘上端空白
BLANK_W = 150 #棋盘左端空白
B_H = 4  # 棋盘高
B_W = 4  # 棋盘宽
UNIT = 90  # 棋盘每格大小
P_S = 60 #棋子大小

class Cshower(tk.Tk):
    def __init__(self):
        super(Cshower, self).__init__()
        self.title('六子棋')
        self.geometry('{0}x{1}'.format(600, 600))
        self.flag=0
        self.matrix=[[1,1,1,1],[1,0,0,1],[-1,0,0,-1],[-1,-1,-1,-1]]
        self.redraw(self.matrix)

    def redraw(self,x):
        #画布
        self.canvas = tk.Canvas(self, bg='white', height=600, width=600)
        #棋盘
        for c in range(BLANK_W, BLANK_W+B_W* UNIT, UNIT):
            x0, y0, x1, y1 = c, BLANK_H, c, BLANK_H+(B_H-1) * UNIT
            self.canvas.create_line(x0, y0, x1, y1,width=2)
        for r in range(BLANK_H, BLANK_H+B_H* UNIT, UNIT):
            x0, y0, x1, y1 = BLANK_W, r, BLANK_W+(B_W-1)* UNIT, r
            self.canvas.create_line(x0, y0, x1, y1,width=2)
        #棋子
        for c in range(0,B_H):
            for r in range(0,B_W):
                if x[c][r]==1:
                    self.oval = self.canvas.create_oval(BLANK_H+r*UNIT-P_S//2, BLANK_W+c*UNIT-P_S//2, BLANK_H+r*UNIT+P_S//2, BLANK_W+c*UNIT+P_S//2, outline='', fill='blue')
                if x[c][r]==-1:
                    self.oval = self.canvas.create_oval(BLANK_H+r*UNIT-P_S//2, BLANK_W+c*UNIT-P_S//2, BLANK_H+r*UNIT+P_S//2, BLANK_W+c*UNIT+P_S//2, outline='', fill='red')
        #选择框
        self.rect=self.canvas.create_rectangle(BLANK_H+r*UNIT-P_S//2-2, BLANK_W+c*UNIT-P_S//2-2, BLANK_H+r*UNIT+P_S//2+2, BLANK_W+c*UNIT+P_S//2+2, outline='black')
        #开始画
        self.canvas.pack()
        #开始监听鼠标左键
        self.canvas.bind('<Button-1>', self.OnB1)

    def OnB1(self,event):
        if self.flag==0:
            self.oval=self.canvas.find_closest(event.x,event.y)
            if self.canvas.itemcget(self.oval,'fill')=='red':
                self.flag=1
                #print (self.canvas.itemcget(self.oval,'bbox'))
        #self.canvas.delete(self.rect)
        #self.rect = self.canvas.create_rectangle(event.x-P_S//2-2,event.y-P_S//2-2, event.x+P_S//2+2, event.y+P_S//2+2,outline='black')
        self.canvas.coords(self.rect, (event.x-P_S//2-2,event.y-P_S//2-2, event.x+P_S//2+2, event.y+P_S//2+2))

                #elseif self.flag==1:
        #    if event.x
        #app.canvas.move(app.oval, 10, 10)self.oval

        print(self.oval)

    #def mouse2matrix(self,(x,y)):
    #def matrix2




