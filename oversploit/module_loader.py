import importlib.util
import os

class ModuleLoader:
    def __init__(self):
        self.module = None

    def load(self, path):
        parts = path.split("/")
        if len(parts) < 2:
            print("[!] Invalid module path. Use format: exploit/test_module")
            return None

        category, name = parts[0], parts[1]
        file_path = os.path.join("modules", category, f"{name}.py")

        if not os.path.exists(file_path):
            print(f"[!] Module not found: {file_path}")
            return None

        spec = importlib.util.spec_from_file_location(f"{category}.{name}", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.module = module.Exploit()
        return self.module
