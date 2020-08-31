#https://docs.python.org/3/library/threading.html
import socket, threading
#TCP ports
def tcp_connect(ip, port_number, delay, output):
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_sock.settimeout(delay)
    try:
        tcp_sock.connect((ip, port_number))
        output[port_number] = True
    except:
        output[port_number] = False
def scan_ports(portrange, host_ip, delay):
    threads = []
    output = {}
    print("Running against:" + host_ip + " with a " + str(delay) + " second delay.")
    
    # create threads for each
    for i in range(portrange):
        t = threading.Thread(target=tcp_connect, args=(host_ip, i, delay, output))
        threads.append(t)
    for i in range(portrange):
        threads[i].start()
    # Locking the main thread until all threads complete
    for i in range(portrange):
        threads[i].join()
    # show whats open
    for i in range(portrange):
        if output[i]:
            print(str(i) + ': ' + str(output[i]))
host_ip = input("Enter host IP: ")    
#https://www.bleepingcomputer.com/tutorials/tcp-and-udp-ports-explained/#:~:text=You%20can%20have%20a%20total,port%20on%20its%20own%20computer.
portrange = 10000
delay = int(input("How many seconds the socket is going to wait until timeout: "))   
scan_ports(portrange, host_ip, delay)