#Run in VM console ipconfig (if VM is Windows) or ifconfig (if VM is Linux).
#IP of eth0 is the IP address that you are looking for.
#192.168.200.224
#https://docs.python.org/3/library/socket.html
import socket
#https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
portrange = int(input("Which port? "))
host_ip = input("Enter host IP: ")    
delay = int(input("How many seconds the socket is going to wait until timeout: "))   
print("Running against:" + host_ip + " with a " + str(delay) + " second delay.")
#TCP ports.
def tcp_connect(ip, port_number, delay):
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_sock.settimeout(delay)
    try:
        tcp_sock.connect((ip, port_number))
        output = True
    except:
        output = False
    return output
#scanner
def scan_ports(portrange, host_ip, delay):
    output_result = tcp_connect(host_ip, portrange, delay)
    print(str(portrange) + ': ' + str(output_result))
scan_ports(portrange, host_ip, delay)




