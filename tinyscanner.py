import argparse
from datetime import datetime
import socket
import sys


def scan_tcp(host, port, only_open=False):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is open (TCP)")
    elif not only_open:
        print(f"Port {port} is closed (TCP)")
    s.close()


def scan_udp(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)

    try:
        s.sendto(b"ping", (host, port))
        data, addr = s.recvfrom(1024)
        print(f"Port {port} is open (UDP)")
    except socket.timeout:
        print(f"Port {port} is open/filtered (UDP)")
    except socket.error as e:
        if e.errno == 111:
            print(f"Port {port} is closed (UDP)")
        else:
            print(f"Error scanning port {port}: {e}")
    finally:
        s.close()


def main():
    parser = argparse.ArgumentParser(
        description="Tiny port scanner simulation.",
        usage="tinyscanner [OPTIONS] [HOST] [PORT]",
    )
    parser.format_usage()
    # Add mutually exclusive group for -t and -u flags
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--udp", help="Perform UDP scan", action="store_true")
    group.add_argument("-t", "--tcp", help="Perform TCP scan", action="store_true")

    parser.add_argument("host", help="Host to scan")
    parser.add_argument(
        "-p",
        "--port",
        help="Port or range of ports to scan (e.g., 80 or 80-83)",
        required=True,
    )
    parser.add_argument(
        "-op", "--only_open", help="Lists only the open ports", action="store_true"
    )

    args = parser.parse_args()

    # Handle port range or single port
    if "-" in args.port:
        start_port, end_port = map(int, args.port.split("-"))
    else:
        start_port = end_port = int(args.port)

    # Perform TCP or UDP scan based on provided flags
    try:
        if args.udp:
            print(f"Scanning for open ports on {args.host}...")
        if args.tcp:
            print(f"Scanning for open ports on {args.host}...")
        for port in range(start_port, end_port + 1):
            if args.udp:
                scan_udp(args.host, port)
            if args.tcp:
                scan_tcp(args.host, port, args.only_open)
    except KeyboardInterrupt:
        print("\nScan interrupted by user. Exiting...")
        sys.exit(0)  # Exit the program cleanly


if __name__ == "__main__":
    main()
