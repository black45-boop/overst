import re

class Exploit:
    name = "Hash Identifier"
    description = "Identifies the most likely hash algorithm based on hash length and format"
    options = {
        "HASH": ""
    }

    def run(self):
        hash_input = self.options["HASH"].strip().lower()

        if not hash_input:
            print("[!] Please provide a hash using: set HASH <value>")
            return

        length = len(hash_input)

        print(f"[*] Analyzing hash: {hash_input}")
        print(f"[*] Length: {length}")

        candidates = []

        if re.match(r"^[a-f0-9]{32}$", hash_input):
            candidates.append("MD5")
        if re.match(r"^[a-f0-9]{40}$", hash_input):
            candidates.append("SHA1")
        if re.match(r"^[a-f0-9]{64}$", hash_input):
            candidates.append("SHA256")
        if re.match(r"^[a-f0-9]{96}$", hash_input):
            candidates.append("SHA384")
        if re.match(r"^[a-f0-9]{128}$", hash_input):
            candidates.append("SHA512")
        if re.match(r"^\$2[aby]?\$.{56}$", hash_input):
            candidates.append("bcrypt")
        if re.match(r"^\$argon2", hash_input):
            candidates.append("Argon2")
        if re.match(r"^[a-f0-9]{16}$", hash_input):
            candidates.append("MySQL 3.x")

        if candidates:
            print("[+] Possible hash types:")
            for c in candidates:
                print(f"    - {c}")
        else:
            print("[!] Unknown or unsupported hash format.")
