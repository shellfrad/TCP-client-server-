from socket import *
import sys

def main(): 
    
    content = open(sys.argv[1], 'r')
    for line in content:
        if not(line == ""):
            serverName = '127.0.0.1'
            serverPort = 61234
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((serverName,serverPort)) 
            clientSocket.send(line.encode())
            reply = clientSocket.recv(1024).decode()
            res, statusCode = reply.split()
            sc = int(statusCode)
            if(sc == 200):
                print("Result is " + res)
            elif(sc == 630):
                print("Error 630: Invalid operands")
            elif(sc == 620):
                print("Error 620: Invalid operation code")
        else: 
            clientSocket.close()
    clientSocket.close()
    content.close()

if __name__ == "__main__":
    main()