import socket

class Exploit:
    name = "TCP Port Scanner"
    description = "Scans open TCP ports on the target host."
    options = {
        "RHOST": "127.0.0.1",
        "PORTS": "21,22,23,80,443,3306"
    }

    def run(self):
        rhost = self.options["RHOST"]
        ports = self.options["PORTS"]

        print(f"[*] Scanning {rhost} on ports: {ports}")
        port_list = [int(p.strip()) for p in ports.split(",")]

        for port in port_list:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)
                    result = sock.connect_ex((rhost, port))
                    if result == 0:
                        print(f"[+] Port {port} is OPEN")
                    else:
                        print(f"[-] Port {port} is closed")
            except Exception as e:
                print(f"[!] Error on port {port}: {e}")
