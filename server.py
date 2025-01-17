import socket as soc
import threading as th
from aux_func import *

display()
print("THIS IS THE ADMIN PANEL. ALL LOGS CAN BE FOUND HERE.\n")
print("Welcome Admin. You can view the logs below.\nLOGS:\n")

def handle_client(client,address):
    while True:
        data = c.recv(1024).decode('ascii')
        info = list()
            
        if(not data):
            print("Client has disconnected.")
            break 
        else:
            info = data.split(',')
            operations = info[0]
            print(f"Choice Received for {info[3]}: {operations.capitalize()} Booking.\n")

        if(operations == "car"):
            s1 = soc.socket()
            s1.connect(('127.0.0.1', 2000))
            s1.send(str(info[1]+','+info[2]+','+info[3]).encode('ascii'))
            result = s1.recv(1024).decode('ascii')
            print(f"Result: {result}\n")
            s1.close()

        elif(operations == "hotel"):
            s2 = soc.socket()
            s2.connect(('127.0.0.1', 6000))
            s2.send(str(info[1]+','+info[2]+','+info[3]).encode('ascii'))
            result = s2.recv(1024).decode('ascii')
            print(f"Result: {result}\n")
            s2.close()

        elif (operations == "flight"):
            s3 = soc.socket()
            s3.connect(('127.0.0.1', 4000))
            s3.send(str(info[1]+','+info[2]+','+info[3]).encode('ascii'))
            result = s3.recv(1024).decode('ascii')
            print(f"Result: {result}\n")
            s3.close()

        else:
            result = ""
        c.send(str(result).encode('ascii'))

    c.close()
            
if __name__ == "__main__":
    s =  soc.socket()
    port = 4328
    s.bind(('127.0.0.1', port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        client_thread = th.Thread(target=handle_client, args=(c, addr))
        client_thread.start()