from pathlib import Path
import ast
import sys
import re

requirements = {
    re.split(r"[<>=]", line.strip())[0].lower()
    for line in Path("requirements.txt").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#")
}

imports = set()

for py_file in Path("src").rglob("*.py"):
    tree = ast.parse(py_file.read_text(encoding="utf-8"))

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.add(name.name.split(".")[0].lower())

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0].lower())

STDLIB = set(sys.stdlib_module_names)

LOCAL_MODULES = {"src", "tests"}
IGNORE = {
    "json",
    "pathlib",
    "ast",
    "dataclasses",
}

imports = {
    i for i in imports if i not in STDLIB and i not in LOCAL_MODULES and i not in IGNORE
}

missing = imports - requirements

if missing:
    print("Missing dependencies:")
    for dep in sorted(missing):
        print("-", dep)
    raise SystemExit(1)

print("Requirements check passed")
