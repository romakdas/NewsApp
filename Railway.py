from tkinter import *
import requests
class Irctc:
    def _init_(self):

       

        self.root=Tk()

        self.root.title("Train Route")

        self.root.minsize(300,500)
        self.root.maxsize(500,700)

        self.root.configure(background="#2F4F4F") #background color


        self.lable1=Label(self.root,text="Train Route",bg="#DAA520",fg="#000000")
        self.lable1.configure(font=("constantia",22,"bold"))
        self.lable1.pack(pady=(30,10))

        self.trainNo=Entry(self.root)
        self.trainNo.pack(ipadx=30,ipady=5)

        self.click=Button(self.root,text="Fetch Station",bg="#A52A2A",fg="#000",width=25,height=2,command=lambda:self.__fetch())
        self.click.pack(pady=(10,20))

        self.result=Label(self.root,text="",bg="#2F4F4F",fg="#ffffff")
        self.result.configure(font=("constantia",10))
        self.result.pack(pady=(5,10))

        self.root.mainloop()

    def __fetch(self):
        train=self.trainNo.get()
        print(train)
        url="https://api.railwayapi.com/v2/route/train/{}/apikey/likbr1rg3b/".format(train)
        response=requests.get(url)
        data=response.json()
        print(data)
a=Irctc()
