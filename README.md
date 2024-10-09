
# Tiny Port Scanner

**Tiny Port Scanner** is a simple Python-based command-line tool that scans TCP and UDP ports on a target host to check if they are open or closed. It supports scanning both single ports and port ranges.

I have also added a way to test the UDP if you know how by using socket 5005 with the socket_manage script. Which you can quickly run in another console to see the UDP scanner working fully!

## Features

- **TCP Scan**: Scan for open TCP ports on a target host.
- **UDP Scan**: Scan for open UDP ports on a target host.
- **Port Range Scanning**: Scan a range of ports (e.g., `80-83`).

## Installation

1. Clone the repository:

   ```bash
   git clone https://01.kood.tech/git/mkuzmina/active.git
   cd tinyscanner
   ```

2. Ensure you have Python 3.x installed.

3. Install any required libraries (if applicable):

   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

   > Note: I suggest using a virtual environment if you are going to do `pip install -e.` because that will add the tiny scanner to your downloaded packages. If neither is wanted then just use `python3 tinyscanner.py` to execute the code!

## Usage

To see all the available options, use the `--help` flag:

```bash
$> tinyscanner --help
usage: tinyscanner [OPTIONS] [HOST] [PORT]

Tiny port scanner simulation.

positional arguments:
  host                  Host to scan

options:
  -h, --help            show this help message and exit
  -u, --udp             Perform UDP scan
  -t, --tcp             Perform TCP scan
  -p PORT, --port PORT  Port or range of ports to scan (e.g., 80 or 80-83)
  -op, --only_open      Lists only the open ports
```

### Examples

1. **UDP Scan on a Single Port**:

   ```bash
   $> tinyscanner -u 127.0.0.1 -p 5004-5006
   Scanning for open ports on 127.0.0.1...
   Port 5004 is open/filtered (UDP)
   Port 5005 is open (UDP)
   Port 5006 is open/filtered (UDP)
   ```

2. **TCP Scan on a Single Port**:

   ```bash
   $> tinyscanner -t 127.0.0.1 -p 205
   Scanning for open ports on 127.0.0.1...
   Port 205 is closed (TCP)
   ```

3. **TCP Scan on a Range of Ports**:

   ```bash
   $> tinyscanner -t 127.0.0.1 -p 80-83
   Scanning for open ports on 127.0.0.1...
   Port 80 is open (TCP)
   Port 81 is closed (TCP)
   Port 82 is closed (TCP)
   Port 83 is closed (TCP)
   ```

### Command-Line Options

- **`-u`**: Perform a UDP scan.
- **`-t`**: Perform a TCP scan.
- **`-p`**: Specify a port or range of ports (e.g., `80` or `80-83`).
- **`-op`**: Only log out the open results (thus only use if you are testing a range of ports).
- **`HOST`**: The IP address or domain name of the host to scan.
- **`--help`**: Display help information.

## Known Limitations

- UDP ports don't make connections thus I have made it so if no response is recieved by timeout I have made it so that you are told it is either filtered or open. Only time to truly know the port is closed if an error is thrown.
