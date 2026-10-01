import socket

print("LOCAL NETWORK PORT SCANNER")
print("-" * 30)

ip = input("Enter IP address to scan: ")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 8080]

print("\nScanning:", ip)

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED")

    sock.close()

print("\nScan completed.")