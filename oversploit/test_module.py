class Exploit:
    name = "Test Exploit"
    description = "A simple test exploit."
    options = {
        "RHOST": "127.0.0.1",
        "RPORT": "80"
    }

    def run(self):
        rhost = self.options["RHOST"]
        rport = self.options["RPORT"]
        print(f"[!] Exploiting {rhost}:{rport} with test exploit...")
