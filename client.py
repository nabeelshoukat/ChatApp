Server
from socket import *
from threading import *
from tkinter import *

hostSocket = socket(AF_INET,SOCK_STREAM)
var = gethostbyname(gethostname())
msg_list = []
host_ip=var
portNo = 7500
hostSocket.bind((host_ip,portNo))
hostSocket.listen()
print("waiting for a connection...")
def sendMessage():
    msg_list.append(txtYourMessage.get())
    clientMessage = txtYourMessage.get()
    textmessage.insert(END, "\n" + "you:" + clientMessage)
    clientsocket.send(str("Nabeel:"+txtYourMessage.get()).encode("utf-8"))
    txtYourMessage.delete(0, END)
    msg_list.clear()
def sendMessage1(e):
    clientMessage = txtYourMessage.get()

    textmessage.insert(END, "\n" + "you:" + clientMessage)
    clientsocket.send(str("Nabeel:"+clientMessage).encode("utf-8"))
    txtYourMessage.delete(0, END)
window = Tk()
window.title("Server")
textmessage = Text(window, width=50)
textmessage.grid(row=0, column=0, padx=10, pady=10)
txtYourMessage = Entry(window, width=50)
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)
txtYourMessage.focus()
txtYourMessage.bind("<Return>", lambda e:sendMessage1(e))

btnsendmessage = Button(window, text="send", width=16,command=sendMessage)
btnsendmessage.grid(row=2, column=0, padx=10, pady=10)



def clientThread():
    while True:
        message = clientsocket.recv(1024).decode('utf-8')
        # print(str(clientaddress[0])  + str(clientaddress[1] + "says"+str(message)))

        # print(message)
        textmessage.insert(END, "\n" + str(message))

        # clientsocket.send("hi back".encode("utf-8"))

while True:
    clientsocket,clientaddress = hostSocket.accept()

    # clients.add(clientsocket)
    thread = Thread(target=clientThread)
    thread.start()

    window.mainloop()


client

from socket import *
from threading import *
from tkinter import *
import tkinter.messagebox
window = Tk()
window.geometry("500x500")
window.title("Client")
name_list = []
class admin():

    def __init__(self):
        self.loginframe = Frame(window,bg = 'blue',width = 300,height = 400)
        self.loginframe.pack(padx= 100 ,pady=50,ipadx=400,ipady=100 )
        self.labelip = Label(self.loginframe,text = "ip:",bg='blue',fg='white',font =("arial",12))
        self.labelip.grid(row =0, column=0,padx = 0,pady=30)
        self.labelname = Label(self.loginframe,text = "Name:",bg='blue',fg='white',font =("arial",12))
        self.labelname.grid(row =1, column=0,padx= 0 , pady=0)

        self.enteryip = Entry(self.loginframe,width = 15, font =('arial',15))
        self.enteryip.grid(row = 0 , column = 1,pady=50,padx=10)

        self.enteryname = Entry(self.loginframe,width = 15, font =('arial',15))
        self.enteryname.grid(row =1 , column = 1,pady=0,padx=10)

        self.okbtn = Button(self.loginframe , text = "Connect",width = 10,bg='yellow',command = self.connection)
        self.okbtn.grid(row = 2 ,column=1,pady=15,padx=30)
    def connection(self):
        name_list.append(self.enteryname.get())
        print(gethostbyname(gethostname()))
        try:
            self.clientsocket = socket(AF_INET, SOCK_STREAM)
            hostip = str(gethostbyname(gethostname()))
            portno = 7500
            self.clientsocket.connect((hostip, portno))
            print("conected")

            self.loginframe.destroy()
            self.thread()
            self.main_gui()

        except:
            tkinter.messagebox.showerror("Error","Can't Connect to the Server")
    def main_gui(self):
        self.textmessage = Text(window, width=50)
        self.textmessage.grid(row=0, column=0, padx=10, pady=10)
        self.txtYourMessage = Entry(window, width=50)
        self.txtYourMessage.grid(row=1, column=0, padx=10, pady=10)
        self.txtYourMessage.focus()
        self.txtYourMessage.bind("<Return>", lambda e: self.sendMessage1(e))

        self.btnsendmessage = Button(window, text="send", width=16, command=self.sendMessage)
        self.btnsendmessage.grid(row=2, column=0, padx=10, pady=10)

    def recvMessage(self):
        try:
            while True:
                serrverMessage = self.clientsocket.recv(1024).decode('utf-8')
                print(serrverMessage)
                self.textmessage.insert(END, "\n" + str(serrverMessage))
        except:
            pass
    def sendMessage(self):

        self.clientMessage = name_list[0]+":"+self.txtYourMessage.get()
        self.textmessage.insert(END, "\n" "You:" + self.txtYourMessage.get())
        self.clientsocket.send(self.clientMessage.encode("utf-8"))
        self.txtYourMessage.delete(0, END)
    def sendMessage1(self,e):

        self.clientMessage = name_list[0]+":"+self.txtYourMessage.get()
        self.textmessage.insert(END, "\n" "You:" + self.txtYourMessage.get())
        self.clientsocket.send(self.clientMessage.encode("utf-8"))
        self.txtYourMessage.delete(0, END)
    def thread(self):
        recvThread = Thread(target=obj.recvMessage)
        recvThread.daemon = True
        recvThread.start()
obj = admin()
obj.thread()
window.mainloop()

