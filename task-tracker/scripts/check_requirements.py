from pathlib import Path
import ast

requirements = {
    line.strip().split("==")[0].lower()
    for line in Path("requirements.txt").read_text().splitlines()
    if line.strip()
}

imports = set()

IGNORE_IMPORTS = {
    "json",
    "pathlib",
    "ast",
    "dataclasses",
}


for py_file in Path("src").rglob("*.py"):
    tree = ast.parse(py_file.read_text())

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.add(name.name.split(".")[0].lower())

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0].lower())

imports = imports - IGNORE_IMPORTS

missing = imports - requirements

if missing:
    print("Missing dependencies:")
    for dep in sorted(missing):
        print("-", dep)

    raise SystemExit(1)

print("Requirements check passed")