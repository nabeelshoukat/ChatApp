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
