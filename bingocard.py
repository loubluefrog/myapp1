from tkinter import *
import os
import random

class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()


    def init_window(self):
        self.master.title("Final Exam A")
        
        
        self.b = (1, 15)
        self.blist =[item for item in range(self.b[0], self.b[1]+1)]
        self.i = (16,30)
        self.ilist =[item for item in range(self.i[0], self.i[1]+1)]
        self.n = (31,45)
        self.nlist =[item for item in range(self.n[0], self.n[1]+1)]
        self.g = (46, 60)
        self.glist =[item for item in range(self.g[0], self.g[1]+1)]
        self.o = (61, 75)
        self.olist =[item for item in range(self.o[0], self.o[1]+1)]
        
        self.bingolist = ['B','I','N','G','O']
        
        self.label = [None for _ in range(5)]
        self.btnb = [None for _ in range(5)]
        self.btni = [None for _ in range(5)]
        self.btnn = [None for _ in range(5)]
        self.btng = [None for _ in range(5)]
        self.btno = [None for _ in range(5)]
        self.frmalpha = Frame(self)


        self.buttons(0,0,self.blist)
        #print(self.blist)
        self.buttons(0,1,self.ilist)
        #print(self.ilist)
        self.nbuttons(0,2,self.nlist)
        #print(self.nlist)
        self.buttons(0,3,self.glist)
        #print(self.glist)
        self.buttons(0,4,self.olist)
        #print(self.olist)
        

        
    def buttons(self, x, y,z):
        a = IntVar()
        b = []
        t = (self.bingolist[y])
        self.label[y] = Label(self.frmalpha, text = self.bingolist[y],
                                      font = 'times 20 bold', fg = 'white',bg = 'blue',
                                      highlightcolor = 'blue', bd = 4,
                                      width = 3, height = 1, relief = 'raised')
        self.label[y].grid(row = x, column = y)
        x+=1
        
        self.index = random.sample(range(15),5)

        for i in range(5):
            u = self.index[i]
            a = z[u]
            self.btnb[i] = Button(self.frmalpha, text = a,
                                      font = 'times 20 bold', fg = 'blue',
                                      width = 3, height = 1)
            self.btnb[i].grid(row = x, column = y)
            x+=1
                
    def nbuttons(self, x,y,z):
        a = IntVar()
        b = []
        t = (self.bingolist[y])
        self.label[y] = Label(self.frmalpha, text = self.bingolist[y],
                                      font = 'times 20 bold', fg = 'white',bg = 'blue',
                                      highlightcolor = 'blue', bd = 4,
                                      width = 3, height = 1, relief = 'raised')
        self.label[y].grid(row = x, column = y)
        x+=1
        
        self.index = random.sample(range(15),5)

        for i in range(4):
            if x!=3:
                u = self.index[i]
                a = z[u]
                self.btnb[i] = Button(self.frmalpha, text = a,
                                          font = 'times 20 bold', fg = 'blue',
                                          width = 3, height = 1)
                self.btnb[i].grid(row = x, column = y)
                x+=1
            if x == 3:
                u = self.index[i]
                a = z[u]
                self.btnb[i] = Button(self.frmalpha,width = 3, height = 1)
                self.btnb[i].grid(row = x, column = y)
                x+=1
            
  
        self.frmalpha.pack()
        self.pack()
        
root = Tk()
root.geometry("300x315")
app = Window(root)
root.mainloop()
