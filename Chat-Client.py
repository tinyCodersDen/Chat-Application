from tkinter import *
import socket
from threading import Thread
root=Tk()
host='localhost'  # server side ip address
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Master=Frame(root)
def recieve_message():
    while True:
        data = s.recv(1024).decode('utf-8')
        # label=Label(root,text="Server: %s"%str(data))
        # label.pack()
        mylist.insert(END, "Server: %s"%str(data))
def send():
    message=e.get()
    s.send(message.encode())
    # label=Label(root,text="You:%s"%str(message))
    e.delete(0,END)
    mylist.insert(END, "You:%s"%str(message))
recvthread=Thread(target=recieve_message)
recvthread.start()
scroll=Scrollbar(Master)
mylist = Listbox(Master, yscrollcommand = scroll.set )
scroll.config( command = mylist.yview )
scroll.pack( side = RIGHT, fill = Y )
mylist.pack(fill=BOTH,expand=1)
root.geometry("300x300")
root.title("Chat Application_Client")
root.resizable(width=False,height=False)
e=Entry(root)
def cls():
    e.delete(0,END)
button1=Button(root, text="Send",command=send)
e.pack(fill=X,expand=1)
button1.pack()
Master.pack(fill=BOTH,expand=1)
root.mainloop()