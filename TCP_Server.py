from socket import *

def main(): 
    try:
        while True:
            serverPort = 61234
            serverSocket = socket(AF_INET,SOCK_STREAM)
            serverSocket.bind(('localhost',serverPort))
            serverSocket.listen(1)
            print ("The server is ready to receive")
            while True:
                connectionSocket, addr = serverSocket.accept()
                message = connectionSocket.recv(1024).decode()
                op, int1, int2 = message.split() 
                if ('.' in int1) or ('.' in int2):
                    statusCode = 630
                    res = -1
                    print(message.strip(),"->",statusCode,res)
                    finalRes = str(res) + " " + str(statusCode)
                    connectionSocket.send(finalRes.encode())
                    connectionSocket.close()
                else:
                    num1 = int(int1)
                    num2 = int(int2)
                    if isValid(op) and isValidNums(num1) and isValidNums(num2):
                        res = preformOperations(op, num1, num2)
                        statusCode = 200
                    elif not (isValid(op)):
                        statusCode = 620
                        res = -1
                    elif op == '/' and int2 == 0:
                        statusCode = 630
                        res = -1
                    print(message.strip(),"->",statusCode,res)
                    finalRes = str(res) + " " + str(statusCode)
                    connectionSocket.send(finalRes.encode())
                    connectionSocket.close()
    except KeyboardInterrupt:
        print("connection closed")
        connectionSocket.close()

def isValid(operationCode): 
    if(not(operationCode == '+' or operationCode == '-' or operationCode == '/' or operationCode == '*')): 
        return False
    else:
        return True

def preformOperations(op, int1, int2):
    if op == '+':
        return int1 + int2
    elif op == '-':
        return int1 - int2
    elif op == '*':
        return int1 * int2
    elif op == '/':
        return int1 / int2

def isValidNums(num): 
    if(isinstance(num, int)):
        return True
    else: 
        return False

if __name__ == "__main__":
    main()