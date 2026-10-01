# cyber-security-task-1# Local IP Port Scanner

  Project Description

This project is a simple Python-based **Local IP Port Scanner**.  
It checks a list of commonly used network ports and identifies whether each port is **OPEN** or **CLOSED** on the given local IP address.

 Objective

The main objective of this project is to understand basic network programming in Python using the `socket` module.

Technologies Used

- Python
- Socket Programming
- Pydroid 3
- GitHub

Features

- Takes the local IP address as input.
- Scans commonly used ports.
- Uses socket connections to check port status.
- Displays whether each port is OPEN or CLOSED.
- Shows a message after the scan is completed.

Ports Scanned

The program checks the following ports:

- 21
- 22
- 23
- 25
- 53
- 80
- 110
- 139
- 443
- 445
- 8080

How to Run

1. Install Python or Pydroid 3.
2. Copy the Python code into a `.py` file.
3. Run the program.
4. Enter the local IP address when prompted.

Example

```text
Enter local IP address: 192.168.1.1

Scanning: 192.168.1.1

Port 21 is CLOSED
Port 22 is OPEN
Port 80 is OPEN
Port 443 is CLOSED

Scan completed.