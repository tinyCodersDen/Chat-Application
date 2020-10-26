from tkinter import *
import socket
from threading import Thread
host=''
port=12345
root=Tk()
Master=Frame(root)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
print('socket binded to', port)
print("Server is waiting for Client")
backlog = 5
s.listen(backlog)
conn,addr = s.accept()
print ('socket is listening')
print ("Got connection from",addr)
def recieve_function():
    while True:
        data=conn.recv(1024).decode('utf-8')
        # label=Label(root,text="Client: %s"%str(data))
        # label.pack()
        mylist.insert(END, "Client: %s"%str(data))
        scroll.config( command = mylist.yview )
def send_message():
    name=e.get()
    conn.send(name.encode())
     #label=Label(root,text="You: %s"%str(name))
     #label.pack()
    mylist.insert(END, "You: %s"%str(name))
    e.delete(0,END)
recvthread=Thread(target=recieve_function)
recvthread.start()
scroll=Scrollbar(Master)
mylist = Listbox(Master, yscrollcommand = scroll.set )
scroll.pack( side = RIGHT, fill = Y )
mylist.pack(fill=BOTH,expand=1)
scroll.config( command = mylist.yview )
root.geometry("300x300")
root.title("Chat Application")
root.resizable(width=False,height=False)
e=Entry(root)
def cls():
    e.delete(0,END)
button1=Button(root, text="Send",command=send_message)
e.pack(fill=X,expand=1)
button1.pack()
Master.pack(fill=BOTH,expand=1)
root.mainloop()