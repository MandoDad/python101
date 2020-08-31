import socket, threading
def main():
    host_ip = input("Enter host IP: ")    
    one_port = input("One Port? Y or N: ").startswith('Y')
    portrange = 10000
    if one_port:
        portrange = int(input("Which port? "))
    delay = int(input("How many seconds the socket is going to wait until timeout: "))   
    scan_ports(one_port, portrange, host_ip, delay)
def tcp_connect(ip, port_number, delay, output):
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_sock.settimeout(delay)
    try:
        tcp_sock.connect((ip, port_number))
        output[port_number] = True
    except:
        output[port_number] = False
def scan_ports(one_port, portrange, host_ip, delay):
    threads = []
    output = {}
    print("Running against:" + host_ip + " with a " + str(delay) + " second delay.")
    
    if one_port:
        tcp_connect(host_ip, portrange, delay, output)
        print(str(portrange) + ': ' + str(output[portrange]))    
    else:
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
main()