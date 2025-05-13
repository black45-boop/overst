import cmd
import os
from core.module_loader import ModuleLoader

class OverSploitCLI(cmd.Cmd):
    prompt = 'OverSploit > '

    def __init__(self):
        super().__init__()
        self.loader = ModuleLoader()
        self.current_module = None

    def do_use(self, arg):
        """Use a specific module: use <module_path>"""
        try:
            self.current_module = self.loader.load(arg)
            print(f"[+] Loaded module: {self.current_module.name}")
            for key, value in self.current_module.options.items():
                print(f"    {key} = {value}")
        except Exception as e:
            print(f"[!] {e}")

    def do_set(self, arg):
        """Set a module option: set <option> <value>"""
        if self.current_module:
            parts = arg.split(" ", 1)
            if len(parts) == 2:
                key, value = parts
                if key in self.current_module.options:
                    self.current_module.options[key] = value
                    print(f"[+] {key} set to {value}")
                else:
                    print(f"[!] Unknown option: {key}")
            else:
                print("[!] Usage: set <option> <value>")
        else:
            print("[!] No module loaded.")

    def do_run(self, arg):
        """Run the currently loaded module"""
        if self.current_module:
            self.current_module.run()
        else:
            print("[!] No module loaded.")

    def do_exit(self, arg):
        """Exit OverSploit"""
        print("Exiting...")
        return True

    def list_modules_by_category(self, category):
        base_path = os.path.join("modules", category)
        if not os.path.exists(base_path):
            print(f"[!] No such category: {category}")
            return

        print(f"[*] {category.capitalize()} Modules:\n")
        for file in os.listdir(base_path):
            if file.endswith(".py") and not file.startswith("__"):
                name = file.replace(".py", "")
                print(f"  - {category}/{name}")

    def do_show(self, arg):
        """Show available modules by category"""
        arg = arg.strip().lower()

        if arg == "exploits":
            self.list_modules_by_category("exploit")
        elif arg == "payloads":
            self.list_modules_by_category("payloads")
        elif arg == "post":
            self.list_modules_by_category("post")
        else:
            print("[!] Usage: show [exploits | payloads | post]")
