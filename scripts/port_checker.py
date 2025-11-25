#!/usr/bin/env python3

import socket
import sys

def usage():
    print("Usage: python port_checker.py <host> <port>")
    sys.exit(1)

if len(sys.argv) != 3:
    usage()

host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

print(f"Checking {host}:{port}...")

try:
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} on {host} is OPEN.")
    else:
        print(f"Port {port} on {host} is CLOSED or FILTERED.")
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()
