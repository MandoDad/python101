#Run in VM console ipconfig (if VM is Windows) or ifconfig (if VM is Linux).
#IP of eth0 is the IP address that you are looking for.
#https://docs.python.org/3/library/socket.html
#https://docs.python.org/3/library/threading.html
import socket
#https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
#https://www.howtogeek.com/howto/28609/how-can-i-tell-what-is-listening-on-a-tcpip-port-in-windows/
#netstat -a >c:\log.txt
portrange = int(input("Which port? "))
host_ip = input("Enter host IP: ")    
delay = int(input("How many seconds the socket is going to wait until timeout: "))   
output_result = False
print("Running against:" + host_ip + " with a " + str(delay) + " second delay.")
#default address family, default socket type
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SO_REUSEADDR tells the kernel to reuse a local # socket in TIME_WAIT state, without waiting for its natural timeout to expire.
tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_sock.settimeout(delay)
try:
    tcp_sock.connect((host_ip, portrange))
    output_result = True
except:
    output_result = False
print(str(portrange) + ': ' + str(output_result))

