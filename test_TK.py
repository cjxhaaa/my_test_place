#python2
from Tkinter import *


class Model():
    def __init__(self):
        self.top = Tk()
        self.top.geometry('500x300')
        
        self.url = StringVar(self.top)
        self.sizes = StringVar(self.top)
        
        self.label = Label(self.top,text='url:',font='Helvetica -12 bold')
        self.label.pack(fill=Y,expand=1)
        
        self.url_name = Entry(self.top,width=100,textvariable=self.url)
        self.url_name.pack()

        self.label = Label(self.top, text='style:', font='Helvetica -12 bold')
        self.label.pack(fill=Y, expand=1)
        
        self.size_name = Entry(self.top, width=100, textvariable=self.sizes)
        self.size_name.pack()
        
        self.scale = Scale(self.top, from_=10, to=40, orient=HORIZONTAL, command=self.resize)
        self.scale.set(12)
        self.scale.pack(fill=X, expand=1)

        self.work = Button(self.top, text='WORK', command=self.work)
        self.work.pack()
        
        self.quit = Button(self.top,text='QUIT',command=self.top.quit,activeforeground='red',activebackground='white')
        self.quit.pack()

    def resize(self,ev=None):
        self.label.config(font='Helvetica -%d bold' % self.scale.get())
        
    def get_url(self):
        return self.url.get()
    
    def get_sizes(self):
        return self.sizes.get()
    
    def work(self):
        url = self.get_url()
        sizes = self.get_sizes()
        import ipdb
        ipdb.set_trace()
        
def run():
    m = Model()
    mainloop()
    
if __name__ == '__main__':
    run()
