import socket
import threading
from queue import Queue
import sys

# Target configuration
target = "127.0.0.1" # Default to localhost
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            return True
        else:
            return False
    except:
        return False

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        queue.task_done()

if __name__ == "__main__":
    print(f"Starting simple port scan on target: {target}")
    
    # Scanning ports 1 to 1024
    for port in range(1, 1025):
        queue.put(port)

    thread_list = []
    
    # Create 100 threads
    for _ in range(100):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print(f"\nScan Complete. Open ports found: {sorted(open_ports)}")
